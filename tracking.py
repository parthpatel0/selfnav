import cv2
import numpy as np
cap = cv2.VideoCapture(0)

pts = []
while (1):

    # Take each frame
    ret, frameold = cap.read()
    frame = cv2.GaussianBlur(frameold,(5,5),0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([52 , 42 , 126 ])
    upper_blue = np.array([ 163 , 255, 255])
    lower_red = np.array([170,42,126])
    upper_red = np.array([255,255,255])

    mask_r = cv2.inRange(hsv, lower_red, upper_red)
    mask_b = cv2.inRange(hsv, lower_blue, upper_blue)
    (minValr, maxValr, minLocr, maxLocr) = cv2.minMaxLoc(mask_r)
    (minValb, maxValb, minLocb, maxLocb) = cv2.minMaxLoc(mask_b)

    cv2.circle(frame,maxLocr, 20, (0, 0 , 255 ), 2, cv2.LINE_AA)
    cv2.circle(frame, maxLocb, 20, (255, 0,0), 2, cv2.LINE_AA)
    cv2.imshow('Track Laser', frame )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()