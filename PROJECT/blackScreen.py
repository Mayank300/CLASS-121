import cv2  
import numpy as np  
  
video = cv2.VideoCapture(0) 
image = cv2.imread("beach.jpeg") 
  
while True: 
  
    ret, frame = video.read() 
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 
  
  
    upper_black = np.array([104, 153, 70]) 
    lower_black = np.array([30, 30, 0]) 
  
    mask = cv2.inRange(frame, lower_black, upper_black) 
    res = cv2.bitwise_and(frame, frame, mask = mask) 
  
    frame_sub_res = frame - res 
    frame_sub_res = np.where(frame_sub_res == 0, image, frame_sub_res) 
  
    cv2.imshow("video", frame) 
    cv2.imshow("mask", frame_sub_res) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
  
video.release() 
cv2.destroyAllWindows() 
