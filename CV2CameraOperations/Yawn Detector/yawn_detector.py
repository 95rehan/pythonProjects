import cv2
import mediapipe as mp
from math import hypot
import time
import threading
import os

# -------- Alarm Function (Mac Compatible) --------
def play_alarm():
    os.system("afplay /System/Library/Sounds/Glass.aiff")

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

# -------- Settings --------
yawn_threshold = 0.55
frames_open = 0
alarm_on = False

print("Press Q to quit")

def mouth_ratio(landmarks, w, h):
    left = landmarks[61]
    right = landmarks[291]
    top = landmarks[13]
    bottom = landmarks[14]

    lx, ly = int(left.x*w), int(left.y*h)
    rx, ry = int(right.x*w), int(right.y*h)
    tx, ty = int(top.x*w), int(top.y*h)
    bx, by = int(bottom.x*w), int(bottom.y*h)

    hor = hypot(lx-rx, ly-ry)
    ver = hypot(tx-bx, ty-by)

    if hor == 0:
        return 0

    return ver / hor


while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(imgRGB)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            ratio = mouth_ratio(face_landmarks.landmark, w, h)

            if ratio > yawn_threshold:
                frames_open += 1
            else:
                frames_open = 0
                alarm_on = False

            # -------- Trigger Alert --------
            if frames_open > 15:
                # FULL SCREEN RED OVERLAY
                overlay = img.copy()
                overlay[:] = (0, 0, 255)
                alpha = 0.4
                img = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

                cv2.putText(img,
                            "YAWNING ALERT!",
                            (w//6, h//2),
                            cv2.FONT_HERSHEY_DUPLEX,
                            2,
                            (255, 255, 255),
                            4)

                # Play alarm once
                if not alarm_on:
                    alarm_on = True
                    threading.Thread(target=play_alarm).start()

    cv2.imshow("Yawn Alert System", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()