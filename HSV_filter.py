#!/usr/bin/env python
# coding: utf-8

# ## <span style="color:red">Disclaimer:</span> This HSV Filter file is for use in the Depth Estimation Program.

# # This HSV Filter Program is designed to convert a color image into a binary black-and-white image. 

# ### First, import necessary libraries

# In[1]:


import sys
import cv2
import numpy as np
import time


# ### Then, define a HSV Filter Method

# In[2]:


def add_HSV_filter(frame, camera):
    
    #Blurring the frame
    blur = cv2.GaussianBlur(frame,(5,5),0) #Gaussian Blur is applied in order to reduce noise from camera
    
    #Converting RGB to HSV
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    
    #create lower and upper limits for left and right image
    l_b_r = np.array([60,110,50]) #Lower limit for red ball since we are trying to track the color red
    u_b_r = np.array([255,255,255]) #Upper limit for red ball
    l_b_l = np.array([143,110,50]) #Lower limit for red ball
    u_b_l = np.array([255,255,255]) #Upper limit for red ball
    
    
    if(camera==1):
        mask = cv2.inRange(hsv, l_b_r, u_b_r)
    else:
        mask = cv2.inRange(hsv, l_b_l, u_b_l)
    
    #erosion and dilation are performed to reduce the noise of our image
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, note, iterations=2)
    
    return mask


# In[ ]:




