import numpy as np
import cv2


img = np.zeros((300,300,3),np.uint8)
img = cv2.rectangle(img,(0,0),(300,300),(255,255,255),-1)
# draw blue circle
img = cv2.circle(img, (40,40), 30, (255,0,0),-1)
img = cv2.circle(img, (130,150), 30, (255,0,0),-1)
img = cv2.circle(img, (270,250), 30, (255,0,0),-1)

# draw green circle
img = cv2.circle(img, (130,40), 30, (0,255,0),-1)
img = cv2.circle(img, (40,150), 30, (0,255,0),-1)
img = cv2.circle(img, (30,250), 30, (0,255,0),-1)

# draw red circle
img = cv2.circle(img, (230,40), 30, (0,0,255),-1)
img = cv2.circle(img, (240,150), 30, (0,0,255),-1)
img = cv2.circle(img, (120,250), 30, (0,0,255),-1)

cv2.imwrite('smarties_new.jpg',img)
cv2.imshow('image',img)

cv2.waitKey(0)

cv2.destroyAllWindows()