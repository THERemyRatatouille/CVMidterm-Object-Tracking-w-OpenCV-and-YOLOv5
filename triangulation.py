#!/usr/bin/env python
# coding: utf-8

# ## <span style="color:red">Disclaimer:</span> This Triangulation file is for use in the Depth Estimation Program.

# # This Triangulation Program is designed to find the depth of objects tracked with a circle.

# ### First, import necessary libraries

# In[1]:


import sys
import cv2
import numpy as np
import time


# ### Then, define a function that calculates the depth
# 

# In[2]:


def find_depth(circle_right, circle_left, frame_right, frame_left, baseline, f, alpha):
    
    #Convert focal length f from [mm] to [pixel]
    height_right, width_right, depth_right = frame_right.shape
    height_left, width_left, depth_left = frame_left.shape
    
    if width_right == width_left:
        f_pixel = (width_right * 0.5) / np.tan(alpha * 0.5 * np.pi/180) #focal length conversion from mm to pixel
        
    else:
        print("Left and right camera frames do not have the same pixel width ") #both frames must have the same width for triangulation to work
        
    x_right = circle_right[0]
    x_left = circle_left[0]
    
    #Calculate disparity
    disparity = x_left - x_right
    
    #Calculate depth
    zDepth = (baseline*f_pixel)/disparity #Depth in cm
    
    return abs(zDepth)
    

