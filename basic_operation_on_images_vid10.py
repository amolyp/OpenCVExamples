import numpy as np
import cv2
from time import sleep

img = cv2.imread('messe.jpg')
img2 = cv2.imread('lena.jpg')

print(img.shape) #returns a tuple of numbers of rows, columns and no of channels
print(img.size) # returns total number fo pixels is accessed
print(img.dtype) # returns image datatype is obtained

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

# Region Of Interest
#If (x1,y1) and (x2,y2) are the two opposite vertices of plate you obtained, then simply use function:
# roi = img[y1:y2, x1:x2]

ball = img[355:414, 236:305]
cv2.imshow('image',img)
# cv2.waitKey(0)
# for i in range(5):
#     print('sleeping for 1 sec')
#     sleep(1)

#roi = img[y1:y2, x1:x2]
img[201:260, 121:190] = ball

img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))

# dst = cv2.add(img,img2)
dst = cv2.addWeighted(img,0.5,img2,0.5,0)

cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
