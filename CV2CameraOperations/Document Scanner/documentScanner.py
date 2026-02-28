import cv2
import numpy as np
import time

# ---------------- Helper Functions ----------------

def reorder(points):
    points = points.reshape((4, 2))
    new_points = np.zeros((4, 1, 2), dtype=np.float32)

    add = points.sum(1)
    new_points[0] = points[np.argmin(add)]
    new_points[3] = points[np.argmax(add)]

    diff = np.diff(points, axis=1)
    new_points[1] = points[np.argmin(diff)]
    new_points[2] = points[np.argmax(diff)]

    return new_points


def biggest_contour(contours):
    biggest = np.array([])
    max_area = 0

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 5000:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area

    return biggest


# ---------------- Camera ----------------

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not detected")
    exit()

WIDTH, HEIGHT = 800, 600
mode = "live"
captured = None
biggest = None

print("Click CAPTURE → Adjust → Click SAVE")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    display = frame.copy()

    if mode == "live":

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 1)
        edges = cv2.Canny(blur, 150, 200)

        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        biggest = biggest_contour(contours)

        if biggest.size != 0:
            cv2.drawContours(display, biggest, -1, (0, 255, 0), 3)

        # Draw CAPTURE button
        cv2.rectangle(display, (20, 520), (200, 580), (0, 255, 0), -1)
        cv2.putText(display, "CAPTURE", (40, 560),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 0), 2)

    elif mode == "preview":

        display = captured.copy()

        # SAVE button
        cv2.rectangle(display, (20, 520), (150, 580), (255, 0, 0), -1)
        cv2.putText(display, "SAVE", (45, 560),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # RETAKE button
        cv2.rectangle(display, (200, 520), (350, 580), (0, 0, 255), -1)
        cv2.putText(display, "RETAKE", (220, 560),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Document Scanner", display)

    key = cv2.waitKey(1) & 0xFF

    # Mouse click handling
    def mouse(event, x, y, flags, param):
        global mode, captured

        if event == cv2.EVENT_LBUTTONDOWN:

            # Capture click
            if mode == "live" and 20 < x < 200 and 520 < y < 580:
                if biggest is not None and biggest.size != 0:
                    pts1 = reorder(biggest)
                    pts2 = np.float32([[0, 0], [WIDTH, 0],
                                       [0, HEIGHT], [WIDTH, HEIGHT]])

                    matrix = cv2.getPerspectiveTransform(pts1, pts2)
                    warp = cv2.warpPerspective(frame, matrix, (WIDTH, HEIGHT))

                    captured = warp
                    mode = "preview"

            # Save click
            elif mode == "preview" and 20 < x < 150 and 520 < y < 580:
                gray = cv2.cvtColor(captured, cv2.COLOR_BGR2GRAY)
                scan = cv2.adaptiveThreshold(
                    gray, 255,
                    cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                    cv2.THRESH_BINARY,
                    11, 2
                )

                filename = f"scan_{int(time.time())}.png"
                cv2.imwrite(filename, scan)
                print(f"Saved as {filename}")
                mode = "live"

            # Retake click
            elif mode == "preview" and 200 < x < 350 and 520 < y < 580:
                mode = "live"

    cv2.setMouseCallback("Document Scanner", mouse)

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()