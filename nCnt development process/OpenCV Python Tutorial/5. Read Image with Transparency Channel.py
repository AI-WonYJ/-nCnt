import cv2

img = cv2.imread('images\Seoul_NTower.png', cv2.IMREAD_UNCHANGED)

print(img[100][50]) # (100, 50)th position Channel(Red, Green, Blue, Alpha) 불러오기