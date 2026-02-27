import cv2
import mediapipe as mp
from math import hypot
import numpy as np
import os

# -------- Camera --------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not detected")
    exit()

# -------- Mediapipe --------
mpHands = mp.solutions.hands
hands = mpHands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=2
)
mpDraw = mp.solutions.drawing_utils

prev_volume = -1
zoom_factor = 1.0
current_volume = 0

print("✋ Left Hand → Zoom")
print("✋ Right Hand → Volume")
print("Press 'q' to exit")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks and results.multi_handedness:

        for handLms, handedness in zip(
                results.multi_hand_landmarks,
                results.multi_handedness):

            label = handedness.classification[0].label
            lmList = []

            for lm in handLms.landmark:
                lmList.append([int(lm.x * w), int(lm.y * h)])

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            if len(lmList) >= 9:

                x1, y1 = lmList[4]
                x2, y2 = lmList[8]

                cv2.circle(img, (x1, y1), 6, (255, 0, 0), cv2.FILLED)
                cv2.circle(img, (x2, y2), 6, (255, 0, 0), cv2.FILLED)
                cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 3)

                length = hypot(x2 - x1, y2 - y1)

                # -------- LEFT HAND → ZOOM --------
                if label == "Left":
                    zoom_factor = np.interp(length, [20, 220], [1.0, 2.5])
                    zoom_factor = round(float(zoom_factor), 2)

                # -------- RIGHT HAND → VOLUME --------
                if label == "Right":
                    volume = int(np.interp(length, [20, 220], [0, 100]))
                    current_volume = volume

                    if abs(volume - prev_volume) > 3:
                        os.system(
                            f"osascript -e 'set volume output volume {volume}'"
                        )
                        prev_volume = volume

    # -------- Apply Digital Zoom --------
    if zoom_factor > 1.0:
        new_w = int(w / zoom_factor)
        new_h = int(h / zoom_factor)

        x1 = w // 2 - new_w // 2
        y1 = h // 2 - new_h // 2
        x2 = x1 + new_w
        y2 = y1 + new_h

        cropped = img[y1:y2, x1:x2]
        img = cv2.resize(cropped, (w, h))

    # -------- Volume UI --------
    bar_x = w - 80
    bar_top = 100
    bar_bottom = 400

    # Draw volume bar outline
    cv2.rectangle(img, (bar_x, bar_top), (bar_x + 30, bar_bottom), (255, 255, 255), 2)

    # Fill bar based on volume
    vol_bar = np.interp(current_volume, [0, 100], [bar_bottom, bar_top])
    cv2.rectangle(img, (bar_x, int(vol_bar)), (bar_x + 30, bar_bottom), (0, 255, 0), cv2.FILLED)

    # Volume text
    cv2.putText(
        img,
        f"{current_volume} %",
        (bar_x - 10, bar_bottom + 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    # Zoom text
    cv2.putText(
        img,
        f"Zoom: {zoom_factor}x",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Hand Zoom & Volume Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()