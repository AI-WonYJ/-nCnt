import cv2
import numpy as np

#Load YOLO
net = cv2.dnn.readNet("By Yolo\darknet-master\yolov3.weights", "By Yolo\darknet-master\cfg\yolov3.cfg")  # weights, cfg파일을 불러와서 yolo의 네트워크와 연결한다.
classes = []  # class 배열 만들기
with open("By Yolo\darknet-master\data\coco.names", "r") as f:  # coco 파일을 읽어온다.
    classes = [line.strip() for line in f.readlines()]  # 읽어온 coco 파일을 whitespace(공백라인)을 제거하여 classes 배열 안에 넣는다.
layer_names = net.getLayerNames()  # 네트워크의 모드 레이어 이름을 가져와서 layer_names에 넣는다.
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]  # 레이어 중 출력 레이어의 인덱스를 가져와서 output_layers에 넣는다.
colors = np.random.uniform(0, 255, size=(len(classes), 3))  # 클래스의 갯수만큼 랜덤으로 BRG 배열을 생성한다. 한 사물 당 하나의 color만 사용할 수 있도록 해서 구분해야 한다.

# Loading image
img = cv2.imread("By Yolo\sample.jpg")
img = cv2.resize(img, None, fx=1, fy=1)
height, width, channels = img.shape

# Detecting objects
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

# Showing informations on the screen
class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            # Object detected
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            # Rectangle coordinates
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indexes:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[i]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
cv2.imshow("Image", img)
print(classes)
cv2.waitKey(0)
cv2.destroyAllWindows()
