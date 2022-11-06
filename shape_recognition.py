#!/usr/bin/env python
# coding: utf-8

# ## <span style="color:red">Disclaimer:</span> This Shape Recognition file is for use in the Depth Estimation Program.

# # This Shape Recognition Program is designed to detect shapes in an image.

# ### First, import necessary libraries

# In[4]:


import sys
import cv2
import numpy as np
import time
import imutils


# ### Then, define a function that detects circles

# In[6]:


def find_circles(frame, mask):
    
    contours = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    center = None
    
    #Only proceed if at least one contour is found
    if len(contours) > 0:
        #Find the largest contour in the mask, then use that value to find the minimum enclosing circle and centroid
        c = max(contours, key = cv2.contourArea) #Finds the largest contour
        ((x,y),radius) = cv2.minEnclosingCircle(c); #Creates a minimum enclosing circle based on the largest contour
        M = cv2.moments(c) #Finds the center point
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]) )
        
        #Only proceed if the radius is greater than a minimum value
        if radius > 10:
            #Draw the cirle and centroid on the frame and update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius), (0,255,255), 2)
            cv2.circle(frame, center, 5, (0,0,0), -1)
        
    return center        
    
    

