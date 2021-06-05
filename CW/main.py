import cv2
import numpy as np
import time as t

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_file = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
capture = cv2.VideoCapture(0)
t.sleep(2)

# bg = background
bg = 0

for i in range(60):
    # return = ret
    ret, bg = capture.read()

bg = np.flip(bg,axis=1)

while (capture.isOpened()):
    ret,img = capture.read()

    if not ret: 
        break

    img = np.flip(img,axis=1)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,120,50])
    upper_red = np.array([10,255,255])
    mask_1 = cv2.inRange(hsv, lower_red, upper_red)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red = np.array([170,120,70])
    upper_red = np.array([180,255,255])
    mask_2 = cv2.inRange(hsv,lower_red, upper_red)

    mask_1 = mask_2 + mask_1
    
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask_1 = cv2.morphologyEx(mask_1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    mask_2 = np.bitwise_not(mask_1)

    res_1 = cv2.bitwise_and(img,img, mask = mask_2)
    res_2 = cv2.bitwise_and(bg,bg,mask  = mask_1)

    final_output = cv2.addWeighted(res_1, 1, res_2, 1, 0)
    output_file.write(final_output)
    cv2.imshow('magic',final_output)
    cv2.waitKey(1)

capture.release(cv2.destroyAllWindows)