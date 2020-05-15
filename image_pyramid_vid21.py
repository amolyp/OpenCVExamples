import cv2
import numpy as np

#find face in images

img = cv2.imread('cell.jpg')
# img = cv2.imread('lena.jpg')
# lr1 = cv2.pyrDown(img)
# lr2 = cv2.pyrDown(lr1)
#
# hr2 = cv2.pyrUp(lr2)

layer = img.copy()
gp = [layer] #gaussian pyramid array

for i in range(6):
    layer = cv2.pyrDown(layer)
    # layer = cv2.pyrUp(layer)
    gp.append(layer)
    # cv2.imshow(str(i), layer)

layer = gp[5]
cv2.imshow('Upper level Gaussian Pyramid', layer)

lp = [layer]


for i in range(5, 0, -1):
    print(i)
    # gaussian_extended = cv2.pyrUp(gp[i]) # gives error replace with below 2 lines
    size = (gp[i-1].shape[1], gp[i-1].shape[0])
    gaussian_extended = cv2.pyrUp(gp[i], dstsize=size)

    laplacian = cv2.subtract(gp[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)

cv2.imshow('Original image', img)
# cv2.imshow('pyrDown1 image', lr1)
# cv2.imshow('pyrDown2 image', lr2)

# cv2.imshow('pyrUp image', hr2)

cv2.waitKey(0)
cv2.destroyAllWindows()
