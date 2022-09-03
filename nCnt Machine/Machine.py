import cv2
import numpy as np

#Load YOLO
net = cv2.dnn.readNet("By Yolo\darknet-master\yolov3.weights", "By Yolo\darknet-master\cfg\yolov3.cfg")
classes = []
with open("By Yolo\darknet-master\data\coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))