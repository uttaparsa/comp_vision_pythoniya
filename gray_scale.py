import cv2
import numpy as np
img = cv2.imread("./sample-images/img/frog.jpg")

# print(img)
# print(type(img))
print(img.dtype)
# img = img.astype('float64')

img = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
img = img.astype('uint8')

cv2.imshow("my image", img)
cv2.waitKey(0)
