import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    
    ret, current_frame = cap.read()
    if ret:
       
        hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

       
        l_red = np.array([0,50,170])
        u_red = np.array([30,200,255])
        mask1 = cv2.inRange(hsv_frame, l_red, u_red)

      
        l_red = np.array([150,50,70])
        u_red = np.array([180,200,255])
        mask2 = cv2.inRange(hsv_frame, l_red, u_red)

        
        mask = mask1 + mask2 

        
        part1 = cv2.bitwise_and(background, background, mask= mask)
        
       
        red_free = cv2.bitwise_not(mask)

       
        part2 = cv2.bitwise_and(current_frame, current_frame, mask= red_free)


        
        cv2.imshow("cloak", part1 + part2)
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()