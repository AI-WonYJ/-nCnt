import cv2

img = cv2.imread('images\Seoul_NTower.png', cv2.IMREAD_UNCHANGED)

print('Original Dimensiuons  : ', img.shape) # 이미지 Original size 출력

scale_percent = 60 # 크기 계수

width = int(img.shape[1] * scale_percent / 100) # 넓이 변경
height = int(img.shape[0] * scale_percent / 100) # 높이 변경
dim = (width, height) # 출력할 이미지 dimention
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA) # size 변경

print('Resized Dimensions : ', resized.shape) # 변경된 size 출력
cv2.imshow("Resized image", resized) # size 변경된 이미지 출력
cv2.waitKey(0)
cv2.destroyAllWindows()