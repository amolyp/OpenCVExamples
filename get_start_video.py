# video 4 = https://www.youtube.com/watch?v=-RtVZsCvXAQ&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=5

import cv2

cap = cv2.VideoCapture(0)  #open device/webcam by index 0 or -1
# cap = cv2.VideoCapture('lesson35 part 2.mkv') # open file

fourcc = cv2.VideoWriter_fourcc(*'XVID') # or 'X', 'V;
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while (cap.isOpened()): #True
    ret, frame = cap.read()

    if ret == True:
        out.write(frame)

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break;
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

