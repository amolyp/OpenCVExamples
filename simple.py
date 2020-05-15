import cv2

print(cv2.__version__)

img = cv2.imread('lena.jpg',-1)
#print(img)/

cv2.imshow('image',img)
key = cv2.waitKey(0) & 0xff  # wait for key press


if key == 27:   # check if ESC key is pressed
    cv2.destroyAllWindows()
elif key == ord('s') :   #check if s key is press 
    cv2.imwrite('lena_s.png',img)
    cv2.destroyAllWindows()
