import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')
# cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()
ret, frame2 = cap.read()
imgCount  = 0

while cap.isOpened():
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    print("len of contour: ",len(contours))

    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)

        if cv2.contourArea(contour) < 1200:
            continue
        cv2.rectangle(frame1, (x,y), (x+w,y+h), (0, 255,0), 4)

        img = frame1
        # save moving objects from frame as image in testimg folder
        if imgCount < 5:
            img_name = "testimg/image_{}.png".format(imgCount)
            cv2.imwrite(img_name, frame1)
            imgwrite = cv2.imread(img_name)
            imgwrite = imgwrite[y: y+h, x:x+w]
            cv2.imwrite(img_name, imgwrite)

            imgCount += 1

        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)

    # cv2.drawContours(frame1, contour, -1, (0, 255, 0), 2) #apply all contour

    cv2.imshow('feed', frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()