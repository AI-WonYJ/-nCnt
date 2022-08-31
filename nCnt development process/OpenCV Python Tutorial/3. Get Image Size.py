import cv2

img = cv2.imread('images\Seoul_NTower.png', cv2.IMREAD_UNCHANGED) # 이미지파일 alpha channel까지 포함하여 불러오기

dimensions = img.shape # 이미지의 dimension 불러오기

height = img.shape[0] # 높이, Height represents the number of pixel rows in the image or the number of pixels in each column of the image array.
width = img.shape[1] # 넓이, Width represents the number of pixel columns in the image or the number of pixels in each row of the image array.
channels = img.shape[2] # channel, Number of Channels represents the number of components used to represent each pixel.
#In the above example, Number of Channels = 4 represent Alpha, Red, Green and Blue channels.

print('Image Dimension        : ',dimensions)
print('Image Height           : ', height)
print('Image Width            : ', width)
print('Number of Channels     : ', channels)