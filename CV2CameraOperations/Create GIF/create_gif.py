import cv2
import imageio
import numpy as np
import time

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

recording = False
frames = []

button_center = (60, 60)
button_radius = 30

def mouse_click(event, x, y, flags, param):
    global recording, frames

    if event == cv2.EVENT_LBUTTONDOWN:
        dist = ((x - button_center[0]) ** 2 + (y - button_center[1]) ** 2) ** 0.5

        if dist < button_radius:
            if not recording:
                print("Recording started...")
                recording = True
                frames = []
            else:
                print("Recording stopped.")
                recording = False
                if len(frames) > 0:
                    filename = f"recording_{int(time.time())}.gif"
                    imageio.mimsave(filename, frames, fps=10)
                    print(f"GIF saved as {filename}")

cv2.namedWindow("GIF Recorder")
cv2.setMouseCallback("GIF Recorder", mouse_click)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    if recording:
        frames.append(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Draw record button
    if recording:
        cv2.circle(frame, button_center, button_radius, (0, 0, 255), -1)
        cv2.putText(frame, "REC", (30, 130),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        cv2.circle(frame, button_center, button_radius, (0, 0, 255), 3)

    cv2.imshow("GIF Recorder", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()