import numpy as np
import cv2

# img = cv2.imread('lena.jpg',1)  # or use below method to create black image as below
img = np.zeros([512,512,3],np.uint8)

#                   start    end          bgr format linethickness
img = cv2.line(img, (0, 0), (255, 255), (255,0,0), 25 )
img = cv2.arrowedLine(img, (0, 255), (255, 255), (255,0,0), 25 )

img = cv2.rectangle(img, (20,20), (100,100), (0,0,255),-1) # -1 fill rectangle instead of empty box

img = cv2.circle(img, (60,60), 50,(0,255,0), 5)

font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img,"OpenCV", (5,500), font, 3, (0,255,255),5 ,cv2.LINE_AA)
cv2.imshow('image',img)

cv2.imwrite("imgpobjec.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
