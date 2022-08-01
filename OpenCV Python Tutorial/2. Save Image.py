import cv2

gray_img  = cv2.imread('images\Seoul_NTower.png', cv2.IMREAD_GRAYSCALE) # 이미지 gray로 불러오기
status = cv2.imwrite('images\Seoul_NTower_gray.png', gray_img) # grey 이미지 저장
print("Image written to file-system : ", status) # 잘 실행되면 True 출력