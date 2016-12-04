from collections import deque
import numpy as np
import argparse
from imtools import resize
import config as conf
import cv2
import detector
from tracker import Tracker
from drawer import Drawer
import time
import calibration as calib
import sys
import json
import utils

'''******** Get Arguments ****************'''                      
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
                help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=conf.BUFFER_SIZE,
                help="max buffer size")
ap.add_argument("-c", "--config", type=bool, default=False, help="start with calibration mode")
ap.add_argument("-n", "--name", type=str, default='Patient', help="name of the patient")
ap.add_argument("-p", "--protocol", type=str, default='squats', help="name of the protocol")
args = vars(ap.parse_args())

patientName = args["name"]
protocolName = args["protocol"]
                                                            
if not args.get("video", False):
    camera = cv2.VideoCapture(0)
else:
    camera = cv2.VideoCapture(args["video"])

# list of tracked points
pts = deque(maxlen=args["buffer"])

if args.get("config", True):
    print "Enter to config mode"
    calib.calibrateBounds()
    f = open(conf.bounds_filename,'r')
    b = json.load(f)
    f.close()
    colorUpper=tuple(b['upper_bounds'][0])
    colorLower=tuple(b['lower_bounds'][0])

else:
    print "using calibrated file"
    colorLower = conf.BOUNDS_HSV['greenLower']
    colorUpper = conf.BOUNDS_HSV['greenUpper']


#_ Init classes
tracker = Tracker()
drawer = Drawer()
#drawer(conf.CIRCLE_FILL_COLOR, conf.CIRCLE_CONTOUR_COLOR,
#       conf.LINE_COLOR, conf.TRAJECTORY_COLOR, conf.DATE_COLOR, conf.TICKNESS)

# define detection radius
minR = conf.MIN_DETECTION_RADIUS
maxR = conf.MAX_DETECTION_RADIUS

#cv2.namedWindow("Frame", cv2.WINDOW_OPENGL)
cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)

while True:
    # grab the current frame                                                
    (grabbed, frame) = camera.read()
    
    # if we are viewing a video and we did not grab a frame,                
    # then we have reached the end of the video  
    if args.get("video") and not grabbed:
        break
                                                  
    frame = resize(frame, width=600)
    mask = detector.detectColor(frame, colorLower, colorUpper)    
    drawer.drawText(frame, time.strftime("%H:%M:%S"),(20,80))
    drawer.drawText(frame, patientName,(20,50))
    #_ Tracking       
    x,y,center,radius = tracker.trackCircle(mask)
    #filter noise

    #_ Draw
    if radius>minR and radius<maxR:
        drawer.drawCircle(frame, x, y, center, radius)
        pts.appendleft(center)
       
    drawer.drawTrajectory(frame, pts)

    # Filter trajectorie
    #pts = utils.remove_values_from_list(pts, None)
    #tr = np.matrix(list_of_tuples_2_array_of_arrays(pts))
    #filter(tr)
    
    # show the frame to our screen 
    cv2.imshow("Frame", frame)

    # if the 'q' key is pressed, stop the loop
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
                            
camera.release()
cv2.destroyAllWindows()
