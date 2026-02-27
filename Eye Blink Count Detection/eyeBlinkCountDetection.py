import cv2
import mediapipe as mp
import numpy as np
from math import hypot

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

# -------- Blink Variables --------
blink_threshold = 0.22   # adjust if needed
frames_closed = 0
blink_count = 0


def eye_aspect_ratio(landmarks, eye_indices, w, h):
    points = []

    for idx in eye_indices:
        x = int(landmarks[idx].x * w)
        y = int(landmarks[idx].y * h)
        points.append((x, y))

    # vertical distances
    A = hypot(points[1][0] - points[5][0],
              points[1][1] - points[5][1])
    B = hypot(points[2][0] - points[4][0],
              points[2][1] - points[4][1])

    # horizontal distance
    C = hypot(points[0][0] - points[3][0],
              points[0][1] - points[3][1])

    if C == 0:
        return 0

    return (A + B) / (2.0 * C)


print("Blink to count")
print("Press 'q' to quit")

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            landmarks = face_landmarks.landmark

            # MediaPipe eye landmark indices
            left_eye_idx = [33, 160, 158, 133, 153, 144]
            right_eye_idx = [362, 385, 387, 263, 373, 380]

            left_ear = eye_aspect_ratio(landmarks, left_eye_idx, w, h)
            right_ear = eye_aspect_ratio(landmarks, right_eye_idx, w, h)

            ear = (left_ear + right_ear) / 2.0

            # Blink logic
            if ear < blink_threshold:
                frames_closed += 1
            else:
                if frames_closed >= 3:
                    blink_count += 1
                frames_closed = 0

            # Show EAR value
            cv2.putText(frame, f"EAR: {round(ear,3)}",
                        (10, 60),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7, (0, 255, 0), 2)

    cv2.putText(frame,
                f"Blink Count: {blink_count}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2)

    cv2.imshow("Blink Counter (MediaPipe)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()