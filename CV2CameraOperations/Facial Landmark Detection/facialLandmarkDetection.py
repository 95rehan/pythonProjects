import cv2
import mediapipe as mp

# -------- Camera Setup --------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not detected")
    exit()

# -------- MediaPipe Setup --------
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

print("Facial Landmark Detection Started")
print("Press 'Q' to exit")

# -------- Main Loop --------
while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    h, w, _ = img.shape

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(imgRGB)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for landmark in face_landmarks.landmark:
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                cv2.circle(img, (x, y), 1, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Facial Landmark Detection", img)

    key = cv2.waitKey(1) & 0xFF

    # Exit on Q or q
    if key == ord('q') or key == ord('Q'):
        break

# -------- Cleanup --------
cap.release()
cv2.destroyAllWindows()