import cv2
import numpy as np


# print all events in cv2 library
# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)


def click_event(event, x, y, flags, param):
    # print ('flags: '+ str(flags))
    # print ('param: '+ str(param))
    if event == cv2.EVENT_LBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]

        # cv2.circle(img,(x,y),2,(0,0,255),-1)
        mycolorimage = np.zeros((512,512,3),np.uint8)
        mycolorimage[:] = [blue, green, red]

        cv2.imshow('color',mycolorimage)
    # if event == cv2.EVENT_LBUTTONDOWN:
    #     cv2.circle(img,(x,y),3, (0,0,255),-1)  #-1 fills the shape
    #     points.append((x,y))
    #     if len(points) >= 2:
    #         cv2.line(img,points[-1],points[-2],(255,0,0), 5)
    #     cv2.imshow('image',img)

    # if event == cv2.EVENT_LBUTTONDOWN:
    #     print(x,', ',y)
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     strxy = str(x) + ',' + str(y)
    #     cv2.putText(img, strxy, (x,y), font, .4, (255,0,255), 1)
    #     cv2.imshow('image',img)

    # if event == cv2.EVENT_RBUTTONDOWN:
    #     blue = img[y,x,0]   #get pixel color for blue
    #     green = img[y,x,1]   #get pixel color for green
    #     red = img[y,x,2]   #get pixel color for red
    #     font = cv2.FONT_HERSHEY_SIMPLEX
    #     strcol = str(blue) + ',' + str(green) + ',' + str(red)
    #     cv2.putText(img, strcol, (x,y), font, .4, (255,255,255), 1)
    #     cv2.imshow('image',img)


# img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image',img)
points = []
cv2.setMouseCallback('image',click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
