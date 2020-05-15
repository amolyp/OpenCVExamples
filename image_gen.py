import cv2
import numpy as np

img = np.zeros((250,500,3),np.uint8)
img = cv2.rectangle(img,(0,0),(250,250),(0,0,0),-1)
img = cv2.rectangle(img,(250,0),(500,250),(255,255,255),-1)
cv2.imshow('image',img)

cv2.imwrite('image_1.png',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
