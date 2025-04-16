from ultralytics import YOLO

model = YOLO("yolov8n-cls.pt")

model.train(data="C:\\Users\\tanta\\OneDrive\\Desktop\\CodingProjects\\classifier-using-yoloV8\\weather_dataset", epochs=10, imgsz=64)