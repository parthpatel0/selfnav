import cv2
import numpy as np

video = cv2.VideoCapture("ap_road_day.mp4")

while True:
    ret, orig_frame = video.read()
    if not ret:
        video = cv2.VideoCapture("ap_road_day.mp4")
        continue

    frame = cv2.GaussianBlur(orig_frame, (5, 5), 0) #applying blur to smooth edges
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converting to HSV colour space
    #lower_blue = np.array([0, 0, 210])
    #upper_blue = np.array([255, 40 , 255])
    #mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.inRange(hsv, np.array([20, 53, 121]), np.array([168,83, 173]))
    edges = cv2.Canny(mask, 50 , 60)

    lines = cv2.HoughLinesP(edges, 1, np.pi/240, 50,maxLineGap= 40)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("frame", frame)
    cv2.imshow("edges", edges)
    #cv2.imshow("mask",mask)
    key = cv2.waitKey(1)
    if key == 27:
        break
video.release()
cv2.destroyAllWindows()