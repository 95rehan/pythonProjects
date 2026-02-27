import cv2

# -------- Camera --------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not detected")
    exit()

# -------- Load Haar Cascade (Correct Way) --------
faceCascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

print("Press 'q' to quit")

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    if len(faces) == 0:
        cv2.putText(
            img,
            "No Face Found!",
            (20, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    for (x, y, w, h) in faces:

        roi = img[y:y+h, x:x+w]

        # Adjust blur size dynamically
        ksize = (max(31, w//3*2+1), max(31, h//3*2+1))
        blur = cv2.GaussianBlur(roi, ksize, 0)

        img[y:y+h, x:x+w] = blur

        # Optional bounding box
        # cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Face Blur", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()