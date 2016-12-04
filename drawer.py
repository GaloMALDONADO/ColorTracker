import cv2
import numpy as np
import config as conf
''' ---------- DRAWING-----------'''
class Drawer:

    def __init__(self):
        self.circleFillColor = conf.CIRCLE_FILL_COLOR
        self.circleContourColor = conf.CIRCLE_CONTOUR_COLOR
        self.lineColor = conf.LINE_COLOR
        self.trajColor = conf.TRAJECTORY_COLOR
        self.textColor = conf.TEXT_COLOR
        self.tickness = conf.TICKNESS
        self.font = conf.FONT

    def __call__(self, cfc, ccc, lc, tc, dc, tk):
        self.circleFillColor = cfc
        self.circleContourColor = ccc
        self.lineColor = lc
        self.trajColor = tc
        self.textColor = dc
        self.tickness = int(tk)
        
    def setCircleContourColor(self, ccc):
        self.circleContourColor = ccc

    def setCirleFillColor(self,cfc):
        self.circleFillColor = cfc

    def setLineColor(self, lc):
        self.lineColor = lc

    def setTrajColor(self, tc):
        self.trajColor = tc

    def setTickness(self, tk):
        self.tickness = int(tk)

    def drawTrajectory(self, frame, pts):
        # loop over the set of tracked points
        for i in xrange(1, len(pts)):
            # if either of the tracked points are None, ignore
            # them 
            if pts[i - 1] is None or pts[i] is None:
                continue
            # otherwise, compute the thickness of the line and
            # draw the connecting lines 
            #thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
            cv2.line(frame, pts[i - 1], pts[i], self.trajColor, self.tickness)

    def drawCircle(self, frame, x, y, center, radius):
        # draw the circle and centroid on the frame,
        # then update the list of tracked points  
        cv2.circle(frame, (int(x), int(y)), int(radius),
                   self.circleContourColor, self.tickness)
        cv2.circle(frame, center, 5, self.circleFillColor, -1)

    def drawLine(self, frame, pt1, pt2):
        cv2.line(frame, int(pt1), int(pt2), self.lineColor, self.tickness)

    def drawText(self, frame, text, position):
        cv2.putText(frame, text, position, self.font, 1, self.textColor, self.tickness) 
