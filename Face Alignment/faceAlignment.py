import cv2
import mediapipe as mp
import numpy as np
from math import atan2, degrees

# -------- Setup --------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

print("Align your face to center & keep straight")
print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    status = "No Face"
    color = (0, 0, 255)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:

            # Get eye coordinates
            left_eye = face_landmarks.landmark[33]
            right_eye = face_landmarks.landmark[263]

            lx, ly = int(left_eye.x * w), int(left_eye.y * h)
            rx, ry = int(right_eye.x * w), int(right_eye.y * h)

            # Draw eyes
            cv2.circle(frame, (lx, ly), 5, (0, 255, 0), -1)
            cv2.circle(frame, (rx, ry), 5, (0, 255, 0), -1)

            # -------- Angle Check --------
            angle = degrees(atan2(ry - ly, rx - lx))

            # -------- Center Check --------
            face_center_x = int((lx + rx) / 2)
            center_tolerance = 50

            if abs(angle) < 5 and abs(face_center_x - w//2) < center_tolerance:
                status = "ALIGNED"
                color = (0, 255, 0)
            else:
                status = "NOT ALIGNED"
                color = (0, 0, 255)

    # Draw center line
    cv2.line(frame, (w//2, 0), (w//2, h), (255, 255, 255), 1)

    cv2.putText(
        frame,
        status,
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        color,
        3
    )

    cv2.imshow("Face Alignment Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()