import cv2
from ultralytics import YOLO

# -------- Load YOLO Model --------
model = YOLO("yolov8n.pt")   # nano version (fastest)

# -------- Camera --------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

print("Object Detection Started")
print("Press Q to quit")

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)

    # -------- YOLO Detection --------
    results = model(frame, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:

            # Bounding Box
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Confidence
            conf = float(box.conf[0])

            # Class Name
            cls = int(box.cls[0])
            label = model.names[cls]

            # Draw Rectangle
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            # Put Label
            cv2.putText(frame,
                        f"{label} {conf:.2f}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.6,
                        (0, 255, 0),
                        2)

    cv2.imshow("YOLO Object Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()