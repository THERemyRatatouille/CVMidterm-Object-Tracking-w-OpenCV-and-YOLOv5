#!/usr/bin/env python
# coding: utf-8

# # Calculating Horizontal and Vertical Offset from the Center of a Detection

# In[2]:


#import the standard libraries
import sys
import cv2
import math
import numpy as np
import time
import imutils
from matplotlib import pyplot as plt


# In[11]:


def find_HV_angle(frame, camera):
    
    img = cv2.imread(frame)
    cv2.imshow('Image', img)
    
    #Converting the image frame to grayscale
    gryscl = cvtColor(img, cv.COLOR_BGR2GRAY)
    
    #Convert to binary
    _, bin_img = cv.threshold(gryscl, 50, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    
    #Calculate contours
    contours, _ = cv.findContours(bw, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    
    for i, j in enumerate(contours):
        
        #Find area contour
        area = cv.contourArea(j)
        
        #ignore tiny or very large contours
        if area > 100000 or area < 5000:
            continue
 
        min_rect = cv.minAreaRect(c)
        box = cv.boxPoints(rect)
        box = np.int0(box)
        
        cen = (int(rect[0][0]), int(rect[0][1])) #get center value
        w = int(rect[1][0]) #width
        h = int(rect[1][1]) #height
        angle = int(rect[2]) #finds the angle
        
        if w < h:
            angle = 90 - angle
        else: angle *= -1
        
        cv.putText("Angle: " + str(angle) + " degrees", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (124,252,0), 2)
        
        
    
    return angle

