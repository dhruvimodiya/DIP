#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:09:57 2023

@author: bmiit202006100110077
"""

import cv2

img = cv2.imread('black.jpeg',0)
cv2.imshow('original img',img)
height, width=img.shape
#print("pixel value at [1,1]" ,img[1,1])
for row in range(1,height-2,10):
    for i in range(1,width-2,5):
        img[row][i]=255

       
#img[10][10]=255      
cv2.imshow("manipulated img",img)
   
cv2.waitKey(0)
cv2.destroyAllWindows()