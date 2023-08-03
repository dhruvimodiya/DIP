#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 17:28:03 2023

@author: bmiit202006100110077
"""

import cv2
import matplotlib as plt

img = cv2.imread('img.jpeg')
h, w = img.shape[:2]
center = (w / 2 , h / 2)
mat = cv2.getRotationMatrix2D(center,90,1)
rotimg = cv2.warpAffine(img,mat, (h , w))
cv2.imshow('original',img)
cv2.imshow('rotated',rotimg)
cv2.waitkey(0)
cv2.destroyAllWindows()

 

#print(image.shape)
#print(image[0][0])
#print(image)