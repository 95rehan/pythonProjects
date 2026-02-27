import cv2
import numpy as np

# ---------------- Color Dictionary ----------------
def get_color_name(b, g, r):
    colors = {
        "Red": (0, 0, 255),
        "Green": (0, 255, 0),
        "Blue": (255, 0, 0),
        "Yellow": (0, 255, 255),
        "Cyan": (255, 255, 0),
        "Magenta": (255, 0, 255),
        "White": (255, 255, 255),
        "Black": (0, 0, 0),
        "Gray": (128, 128, 128),
        "Orange": (0, 165, 255),
        "Pink": (203, 192, 255),
        "Purple": (128, 0, 128)
    }

    minimum = float("inf")
    color_name = "Unknown"

    for name, (cb, cg, cr) in colors.items():
        d = abs(b - cb) + abs(g - cg) + abs(r - cr)
        if d < minimum:
            minimum = d
            color_name = name

    return color_name


# ---------------- Mouse Callback ----------------
mouse_x, mouse_y = 0, 0

def mouse_move(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x, y


# ---------------- Camera ----------------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not detected")
    exit()

cv2.namedWindow("Live Color Detector")
cv2.setMouseCallback("Live Color Detector", mouse_move)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    if 0 <= mouse_x < w and 0 <= mouse_y < h:
        b, g, r = frame[mouse_y, mouse_x]
        color_name = get_color_name(b, g, r)

        # Draw circle at cursor
        cv2.circle(frame, (mouse_x, mouse_y), 8, (0, 255, 0), 2)

        # Display color name
        cv2.rectangle(frame, (10, 10), (300, 70), (0, 0, 0), -1)
        cv2.putText(
            frame,
            f"{color_name}  BGR: {b},{g},{r}",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

    cv2.imshow("Live Color Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()