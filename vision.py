import cv2
import numpy as np
img = cv2.imread("./sample-images/img/frog.jpg")

# print(img)
# print(type(img))
print(img.dtype)
# img = img.astype('float64')
# img = img * 1.5
# img = np.maximum(0, img)
# img = np.minimum(255, img)

img[:,:,0], img[:,:,1] = img[:,:,1], img[:,:,0]
img = img.astype('uint8')

cv2.imshow("my image", img)
cv2.waitKey(0)
