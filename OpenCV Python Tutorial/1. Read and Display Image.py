import cv2

img = cv2.imread('images\Seoul_NTower.png') # 이미지 불러오기
cv2.imshow('sample image',img) # 이미지 출력하기
cv2.waitKey(0) # 키가 눌릴 때까지 기다리기
cv2.destroyAllWindows() # 키가 눌리면 이미지 지우기