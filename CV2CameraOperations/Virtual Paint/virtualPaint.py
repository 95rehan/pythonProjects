import cv2
import numpy as np

# -------- Camera --------
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)

cap.set(3, frameWidth)
cap.set(4, frameHeight)

# -------- HSV Colors --------
myColors = [
    [5, 107, 0, 19, 255, 255],     # Orange
    [133, 56, 0, 159, 156, 255],   # Purple
    [57, 76, 0, 100, 255, 255]     # Green
]

# BGR paint colors
myColorValues = [
    [0, 140, 255],   # Orange
    [255, 0, 255],   # Purple
    [0, 255, 0]      # Green
]

myPoints = []   # [x, y, colorId]


# -------- Detect Color --------
def findColor(img):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []

    for count, color in enumerate(myColors):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])

        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)

        if x != 0 and y != 0:
            newPoints.append([x, y, count])

    return newPoints


# -------- Get Contour Center --------
def getContours(mask):
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 800:
            x, y, w, h = cv2.boundingRect(cnt)
            return x + w // 2, y

    return 0, 0


# -------- Draw Paint --------
def drawOnCanvas(img):
    for point in myPoints:
        cv2.circle(img, (point[0], point[1]), 10,
                   myColorValues[point[2]], cv2.FILLED)


# -------- Main Loop --------
print("Press Q to Quit")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    imgResult = img.copy()

    # -------- Clear Button --------
    cv2.rectangle(imgResult, (500, 10), (630, 60), (0, 0, 255), cv2.FILLED)
    cv2.putText(imgResult, "CLEAR", (510, 45),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 2)

    newPoints = findColor(img)

    # -------- Add New Points --------
    for newP in newPoints:
        myPoints.append(newP)

        # If finger touches CLEAR button
        if 500 < newP[0] < 630 and 10 < newP[1] < 60:
            myPoints.clear()

    # -------- Draw All Points --------
    drawOnCanvas(imgResult)

    cv2.imshow("Virtual Paint", imgResult)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('q') or key == ord('Q'):
        break

cap.release()
cv2.destroyAllWindows()