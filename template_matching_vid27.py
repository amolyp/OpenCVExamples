import cv2
import numpy as np

# Match template can be used to identify specific cell types in a image and count them


img = cv2.imread('messe5.jpg')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('messe_face.png',0)
#get col and row value in reverse order
w, h =template.shape[::-1]

res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)

print(res)

threshold = 0.95

# find the brightest point in the result matrix
loc = np.where(res >= threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

