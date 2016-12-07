import cv2
bounds_filename = 'outputs/bounds.txt'

COLOR_NAMES_RGB = {
    'Black': (0, 0, 0),
    'NavyBlue': (0, 0, 128),
    'DarkBlue': (0, 0, 139),
    'MediumBlue': (0, 0, 205),
    'Blue':(0, 0, 255),
    'LightSlateBlue':(132, 112, 255),
    'SkyBlue':(135, 206, 235),
    'LightSkyBlue':(135, 206, 250),
    'LightBlue':(173, 216, 230),
    'DarkGreen':(0, 100, 0),
    'LightGreen':(144, 238, 144),
    'Green':(0, 128, 0),
    'Yellow':(255, 255, 0),
    'LightYellow':(255, 255, 224),
    'Red': (255, 0, 0),
    'LightCyan':(224, 255, 255),
    'White':(255, 255, 255) }

BOUNDS_HSV = {
    'greenLower': (29, 86, 6),
    'greenUpper': (64, 255, 255) }

#_ Detection
MIN_DETECTION_RADIUS = 20
MAX_DETECTION_RADIUS = 40

#_ Drawing
CIRCLE_FILL_COLOR = (0,0,255)
CIRCLE_CONTOUR_COLOR = (140,140,140)
LINE_COLOR = (0,0,0)
TRAJECTORY_COLOR = (0,0,0)
TEXT_COLOR = (90,90,90)
TICKNESS = 2
#FONT = cv2.FONT_HERSHEY_PLAIN 
FONT = cv2.FONT_HERSHEY_SIMPLEX 
#_ Tracker
BUFFER_SIZE = 64*10
