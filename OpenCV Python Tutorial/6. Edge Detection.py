import cv2

img = cv2.imread('images\Seoul_NTower.png')
edges = cv2.Canny(img, 100, 200) # 이미지에서 초점이 맞춰진 개체의 가장자리 찾는 구문

cv2.imshow("Edge Detected Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()