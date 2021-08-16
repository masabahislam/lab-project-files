import cv2 as cv
import numpy as np
img=cv.imread('D.jpg',1)

#img = np.zeros([512,512,3],np.uint8)
img = cv.line(img,(0,0),(255,255),(255,255,255),5)
img = cv.arrowedLine(img,(0,255),(255,255),(0,255,0),10)
img = cv.rectangle(img,(384,0),(510,128),(0,0,255))
img = cv.circle(img,(447,63),63,(0,255,0),3)
font = cv.FONT_ITALIC
img = cv.putText(img,'open cv',(10,500),font,4,(0,255,255),10,cv.LINE_4)
cv.imshow('pic name',img)
cv.waitKey(0)
cv.destroyAllWindows()