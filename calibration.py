from colors import Colors
import cv2
import numpy as np
import json
import config

def calibrateBounds():
    #_ Init
    c=Colors()
    bounds = {'lower_bounds':[], 'upper_bounds':[]}

    #_ Get color from palette
    while True:
        try:
            color = c.getRGBfromPalette()
            color2 = np.uint8([[[ color[2], color[1], color[0] ]]])
            hsv = cv2.cvtColor(color2,cv2.COLOR_BGR2HSV).squeeze()
            bounds['lower_bounds'].append((hsv[0]-10, 100, 100))
            bounds['upper_bounds'].append((hsv[0]+10, 255, 255))
        except:
            break
           
    #write in config file
    f = open(config.bounds_filename,'w')
    b = json.dumps(bounds,f)    
    f.write(b)
    f.close()
    print('File %s has been written',config.bounds_filename)
    
