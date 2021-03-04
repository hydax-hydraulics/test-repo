import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while (True):
    _, frame = cap.read()
    cv2.imshow('Orginal',frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',gray)
    template = cv2.imread('phone1.jpg',0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.62
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
       cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

    cv2.imshow('Detected',frame)
    
    
    
  
    
    key = cv2.waitKey(1)
    if key ==27:
        cap.release()

        break

cv2.destroyAllWindows()