import torch
import cv2

# Charger YOLOv5 depuis GitHub
model = torch.hub.load('ultralytics/yolov5:v6.0', 'yolov5s', pretrained=True)
model.eval()

# Capture de la vidéo en direct depuis la caméra
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    results = model(frame)

    # Récupérer les prédictions
    predictions = results.xyxy[0].numpy()

    # Dessiner les bounding boxes sur l'image
    for box in predictions:
        cv2.rectangle(frame, (int(box[0]), int(box[1])), (int(box[2]), int(box[3])), (0, 255, 0), 2)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
