from ultralytics import YOLO
import cv2
model = YOLO('yolo11n.pt')
results = model("C:/Users/valor/PycharmProjects/SIH/imagetest/img1.jpeg", show=True)
cv2.waitKey(0)
