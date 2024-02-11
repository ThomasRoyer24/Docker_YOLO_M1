import torch
import cv2

# Charger YOLOv5 depuis GitHub
model = torch.hub.load('ultralytics/yolov5:v6.0', 'yolov5s', pretrained=True)
model.eval()

# Capture de la vidéo en direct depuis la caméra
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    # Effectuer l'inférence avec YOLOv5
    results = model(frame)

    # Récupérer les prédictions
    predictions = results.xyxy[0].numpy()

    # Modifier la couleur en fonction de la position de la bounding box
    for box in predictions:
        x, y, w, h = int(box[0]), int(box[1]), int(box[2] - box[0]), int(box[3] - box[1])

        # Calculer la composante bleue en fonction de la position x
        blue_component = int(255 * (x / frame.shape[1]))

        # Calculer la composante rouge en fonction de la position y
        red_component = int(255 * (y / frame.shape[0]))

        # Utiliser les composantes pour définir la couleur
        color = (blue_component, 0, red_component)

        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
