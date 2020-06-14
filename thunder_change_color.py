import cv2
import numpy as np
img = cv2.imread('./sample-images/img/raad.jpg')
res,thunder = cv2.threshold(img,215,255,cv2.THRESH_BINARY)
thunder[:,:,0] = img[:,:,0] - (.05*thunder[:,:,0]) # GREEN
thunder[:,:,1] = img[:,:,1] - (.15*thunder[:,:,1]) # BLUE
thunder[:,:,2] = img[:,:,2] - (.55*thunder[:,:,2]) # RED
thunder = thunder.astype('float64')
thunder = thunder * 1.2
thunder = np.maximum(0, thunder)
thunder = np.minimum(255, thunder)


thunder = thunder.astype('uint8')
# thunder += 0.1
cv2.imwrite('res.jpg',thunder)
