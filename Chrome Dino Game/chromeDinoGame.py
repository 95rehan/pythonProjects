import cv2
import mediapipe as mp
import numpy as np
import random
import time
from math import hypot

# ---------------- Camera ----------------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not detected")
    exit()

# ---------------- MediaPipe ----------------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

blink_threshold = 5.5
blink_cooldown = 0.3
last_blink_time = 0

# ---------------- Game Settings ----------------
WIDTH = 900
HEIGHT = 600  # bigger canvas

GAME_HEIGHT = 400  # top half area for game

dino_x = 100
dino_y = 300
dino_size = 40
velocity = 0
gravity = 1.2
jump_strength = -15

obstacles = []
score = 0
game_over = False


def eye_ratio(landmarks, eye_indices, w, h):
    points = []
    for idx in eye_indices:
        x = int(landmarks[idx].x * w)
        y = int(landmarks[idx].y * h)
        points.append((x, y))

    hor = hypot(points[0][0] - points[3][0],
                points[0][1] - points[3][1])
    ver = hypot(points[1][0] - points[5][0],
                points[1][1] - points[5][1])

    if ver == 0:
        return 0

    return hor / ver


print("👁 Blink to Jump")
print("Press 'r' to Restart | 'q' to Quit")

while True:
    ret, cam_frame = cap.read()
    if not ret:
        break

    cam_frame = cv2.flip(cam_frame, 1)
    h_cam, w_cam, _ = cam_frame.shape
    rgb = cv2.cvtColor(cam_frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    # ---------------- Blink Detection ----------------
    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            landmarks = face_landmarks.landmark
            left_eye = [33, 160, 158, 133, 153, 144]

            ratio = eye_ratio(landmarks, left_eye, w_cam, h_cam)

            current_time = time.time()

            if ratio > blink_threshold:
                if current_time - last_blink_time > blink_cooldown:
                    if not game_over:
                        velocity = jump_strength
                    last_blink_time = current_time

    # ---------------- Main Canvas ----------------
    frame = np.ones((HEIGHT, WIDTH, 3), dtype=np.uint8) * 255

    # ---------------- Game Logic ----------------
    if not game_over:
        velocity += gravity
        dino_y += velocity

        if dino_y > 300:
            dino_y = 300
            velocity = 0

        if random.randint(1, 50) == 1:
            obstacles.append([WIDTH, 300])

        for obs in obstacles:
            obs[0] -= 8

        obstacles = [obs for obs in obstacles if obs[0] > -20]

        for obs in obstacles:
            if (dino_x < obs[0] + 20 and
                dino_x + dino_size > obs[0] and
                dino_y + dino_size > obs[1]):
                game_over = True

        score += 1

    # ---------------- Draw Game (Top Area) ----------------
    cv2.line(frame, (0, 340), (WIDTH, 340), (0, 0, 0), 2)

    cv2.rectangle(
        frame,
        (dino_x, int(dino_y)),
        (dino_x + dino_size, int(dino_y + dino_size)),
        (0, 0, 0),
        -1
    )

    for obs in obstacles:
        cv2.rectangle(
            frame,
            (obs[0], obs[1]),
            (obs[0] + 20, obs[1] + 40),
            (0, 150, 0),
            -1
        )

    cv2.putText(
        frame,
        f"Score: {score}",
        (700, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 0),
        2
    )

    if game_over:
        cv2.putText(
            frame,
            "GAME OVER",
            (320, 200),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.5,
            (0, 0, 255),
            3
        )

    # ---------------- Camera Box (Bottom Right) ----------------
    cam_small = cv2.resize(cam_frame, (250, 180))

    y1 = HEIGHT - 190
    y2 = HEIGHT - 10
    x1 = WIDTH - 260
    x2 = WIDTH - 10

    frame[y1:y2, x1:x2] = cam_small

    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 2)

    cv2.imshow("Dino Blink Game", frame)

    key = cv2.waitKey(1)

    if key == ord('r'):
        game_over = False
        obstacles = []
        score = 0
        dino_y = 300
        velocity = 0

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()