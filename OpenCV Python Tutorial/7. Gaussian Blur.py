import cv2
import numpy

src = cv2.imread('images\Seoul_NTower.png', cv2.IMREAD_UNCHANGED)

dst = cv2.GaussianBlur(src,(5,5), cv2.BORDER_DEFAULT) # Gaussian 흐림 효과를 적용

cv2.imshow("Gaussian Smoothing", numpy.hstack((src, dst))) # 원본 이미지와 효과 적용 이미지 출력
cv2.waitKey(0)
cv2.destroyAllWindows()