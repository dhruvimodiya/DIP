#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:39:35 2023

@author: bmiit202006100110077
"""
#blending two image
import cv2
 
img1 = cv2.imread('add.jpeg')
img2 = cv2.imread('img.jpeg')
 
img1 = cv2.resize(img1, (400, 400))
img2 = cv2.resize(img2, (400, 400))
 
result = cv2.addWeighted(img1, 0.3, img2, 0.7, 0.0);
 
cv2.imshow('blend', result)
cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
