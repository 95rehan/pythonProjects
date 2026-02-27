import cv2
import time

duration = 5  # seconds

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

start_time = time.time()

print("Press R to reset")
print("Press Q to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    elapsed = int(time.time() - start_time)
    remaining = duration - elapsed

    if remaining < 0:
        remaining = 0

    cv2.putText(frame,
                f"Timer: {remaining}",
                (50, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                1.5,
                (255, 0, 0),
                3)

    cv2.imshow("Camera Timer", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("r"):   # reset timer
        start_time = time.time()

    if key == ord("q"):   # quit
        break

    if remaining == 0:
        cv2.putText(frame,
                    "Time's Up!",
                    (50, 120),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3)
        cv2.imshow("Camera Timer", frame)
        cv2.waitKey(2000)
        break

cap.release()
cv2.destroyAllWindows()