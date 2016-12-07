import cv2
import drawer


class Tracker:
    def __init__(self):
        self.x = 0.
        self.y = 0.
        self.radius = 0
        self.center = None
    
    def trackCircle(self, mask):
        # find contours in the mask and initialize the current
        # (x, y) center of the ball     
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)[-2]
        self.center = None
        # only proceed if at least one contour was found         
        if len(cnts) > 0:
            # find the largest contour in the mask, then use
            # it to compute the minimum enclosing circle and
            # centroid                                           
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            self.x = x; self.y = y; self.radius = radius
            M = cv2.moments(c)
            self.center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
        return self.x, self.y, self.center, self.radius
