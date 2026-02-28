import cv2
import mediapipe as mp
import time

# -------- Camera Setup --------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

# -------- MediaPipe Hands --------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

mp_draw = mp.solutions.drawing_utils

p_time = 0

print("Hand Landmark Detection Started")
print("Press Q to exit")

# -------- Main Loop --------
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:

        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):

            # Draw landmarks + connections
            mp_draw.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Get hand label (Left/Right)
            if results.multi_handedness:
                label = results.multi_handedness[idx].classification[0].label
                cv2.putText(img, label,
                            (10, 70 + idx*30),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (0, 255, 0),
                            2)

            # Draw each landmark
            for id, lm in enumerate(hand_landmarks.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx, cy), 4, (0, 0, 255), cv2.FILLED)

                # Optional: show landmark ID
                # cv2.putText(img, str(id), (cx, cy),
                #             cv2.FONT_HERSHEY_SIMPLEX,
                #             0.3, (255, 0, 0), 1)

    # -------- FPS Counter --------
    c_time = time.time()
    fps = 1 / (c_time - p_time) if p_time != 0 else 0
    p_time = c_time

    cv2.putText(img, f"FPS: {int(fps)}",
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 0),
                2)

    cv2.imshow("Hand Landmark Detection", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q'):
        break

# -------- Cleanup --------
cap.release()
cv2.destroyAllWindows()