import colorsys
import cv2
import numpy as np
import config as conf

class Colors:

    def __init__(self):
        self.colorsRGB = conf.COLOR_NAMES_RGB
        self.clist = conf.COLOR_NAMES_RGB.keys()
        self.boundsHSV = conf.BOUNDS_HSV

    def getRGBfromName (self, name):
        return self.colorsRGB[name]
    
    def getHSVfromName(self, name):
        rgb = self.getRGBfromName(name)
        return colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
    
    def rgb2HSV(self, rgb):
        return colorsys.rgb_to_hsv(rgb[0],rgb[1],rgb[2])
    
    def hsv2RGB(self, hsv):
        return colorsys.hsv_to_rgb(hsv[0],hsv[1],hsv[2])

    def getRGBfromPalette(self):
        def nothing(x):
            pass

        # Create a black image, a window
        img = np.zeros((300,512,3), np.uint8)
        cv2.namedWindow('image')

        # create trackbars for color change
        cv2.createTrackbar('R','image',0,255,nothing)
        cv2.createTrackbar('G','image',0,255,nothing)
        cv2.createTrackbar('B','image',0,255,nothing)

        # create switch for ON/OFF functionality
        switch = '0 : OFF \n1 : SAVE'
        cv2.createTrackbar(switch, 'image',0,1,nothing)

        while(1):
            cv2.imshow('image',img)

            # get current positions of four trackbars
            r = cv2.getTrackbarPos('R','image')
            g = cv2.getTrackbarPos('G','image')
            b = cv2.getTrackbarPos('B','image')
            s = cv2.getTrackbarPos(switch,'image')
            img[:] = [b,g,r]
            
            if s == 1:
                cv2.destroyWindow('image')
                return (r,g,b)
            
            # if the 'q' key is pressed, stop the loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyWindow('image')
                break

    def getRGBfromFrame(frame, mask):
        pass
