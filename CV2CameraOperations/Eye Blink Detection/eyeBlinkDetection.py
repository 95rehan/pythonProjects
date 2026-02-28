import cv2
import mediapipe as mp
from math import hypot
import numpy as np
import os
import time

# -------- Camera --------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not detected")
    exit()

# -------- MediaPipe --------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

def get_blinking_ratio(landmarks, eye_indices, w, h):
    points = []

    for idx in eye_indices:
        x = int(landmarks[idx].x * w)
        y = int(landmarks[idx].y * h)
        points.append((x, y))

    left_point = points[0]
    right_point = points[3]
    center_top = points[1]
    center_bottom = points[5]

    hor = hypot(left_point[0] - right_point[0],
                left_point[1] - right_point[1])

    ver = hypot(center_top[0] - center_bottom[0],
                center_top[1] - center_bottom[1])

    if ver == 0:
        return 0

    return hor / ver


blink_threshold = 5.0
sound_cooldown = 1.0  # seconds
last_sound_time = 0

print("Press 'q' to quit")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    blink_detected = False

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            landmarks = face_landmarks.landmark

            left_eye = [33, 160, 158, 133, 153, 144]
            right_eye = [362, 385, 387, 263, 373, 380]

            left_ratio = get_blinking_ratio(landmarks, left_eye, w, h)
            right_ratio = get_blinking_ratio(landmarks, right_eye, w, h)

            ratio = (left_ratio + right_ratio) / 2

            if ratio > blink_threshold:
                blink_detected = True

    current_time = time.time()

    if blink_detected:
        # -------- Play Sound (macOS) --------
        if current_time - last_sound_time > sound_cooldown:
            os.system("afplay /System/Library/Sounds/Ping.aiff &")
            last_sound_time = current_time

        # -------- Dark Overlay --------
        overlay = img.copy()
        cv2.rectangle(overlay, (0, 0), (w, h), (0, 0, 0), -1)
        img = cv2.addWeighted(overlay, 0.6, img, 0.4, 0)

        text = "BLINKING"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 3
        thickness = 6

        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = (w - text_size[0]) // 2
        text_y = (h + text_size[1]) // 2

        cv2.putText(img, text,
                    (text_x, text_y),
                    font,
                    font_scale,
                    (0, 255, 0),
                    thickness)

    cv2.imshow("Blink Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()