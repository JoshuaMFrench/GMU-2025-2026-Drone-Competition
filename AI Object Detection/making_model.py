from ultralytics import YOLO

model = YOLO("yolov8n.yaml")

results = model.train(data="C:/Users/conno/Python Files/Python Project/Work/Drone Competiton/Object Tracking/YOLO Files/circle_detection.yaml", epochs=50)