# For webcam
from ultralytics import YOLO

# Load custom trained YOLOv8 model
model = YOLO("yolov8n.pt")

# Use the model to detect object
model.predict(source="0", show=True)