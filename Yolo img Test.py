import cv2
import numpy as np

# Yolo 로드
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg") # weights, cfg파일을 불러와서 yolo의 네트워크와 연결한다.
classes = []
with open ("coco.names", "r") as f: # coco 파일을 읽어온다.
  classes = [line.strip() for line in f.readlines()] # 읽어온 coco 파일을 whitespace(공백라인)를 제거하여 classes 배열 안에 넣는다.
layer_names = net.getLayerNames() # 네트워크의 모든 레이어 이름을 가져와서 layer_names에 넣는다.
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
# 레이어 중 출력 레이어의 인덱스를 가져와서 output_layers에 넣는다.

colors = np.random.uniform(0, 255, size=(len(classes), 3)) # 클래스의 갯수만큼 랜덤으로 BRG 배열을 생성한다. 한 사물 당 하나의 color만 사용할 수 있도록 해서 구분해야 한다.


# 이미지 가져오기
img = cv2.imread("picture2.png") # opencv를 통해 이미지를 가져온다.