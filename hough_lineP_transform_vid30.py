import cv2
import numpy as np

# refer video 28 and 29
img = cv2.imread('road.jpg')
# img = cv2.imread('sudoku.jpg')
# img = cv2.imread('sudoku.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
cv2.imshow('Canny edge', edges)

lines = cv2.HoughLinesP(edges, 1, np.pi /180, 100, minLineLength=100, maxLineGap=10)

print(lines)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0),2)

cv2.imshow('Image', img)

cv2.waitKeyEx(0)
cv2.destroyAllWindows()