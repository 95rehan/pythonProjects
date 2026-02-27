import cv2
import mediapipe as mp

# -------- Camera --------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

# -------- MediaPipe --------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=2,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75
)

mp_draw = mp.solutions.drawing_utils

print("Hand Detection Started")
print("Press Q to exit")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks and results.multi_handedness:

        for hand_landmarks, handedness in zip(
                results.multi_hand_landmarks,
                results.multi_handedness):

            # Draw landmarks
            mp_draw.draw_landmarks(
                img,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            label = handedness.classification[0].label
            score = handedness.classification[0].score

            # Get wrist position to place label near hand
            wrist = hand_landmarks.landmark[0]
            x = int(wrist.x * w)
            y = int(wrist.y * h)

            text = f"{label} Hand ({score:.2f})"

            cv2.putText(img,
                        text,
                        (x - 50, y - 20),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2)

        if len(results.multi_hand_landmarks) == 2:
            cv2.putText(img,
                        "Both Hands Detected",
                        (w//2 - 150, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,
                        (0, 255, 255),
                        2)

    cv2.imshow("Left / Right Hand Detection", img)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q') or key == ord('Q'):
        break

cap.release()
cv2.destroyAllWindows()