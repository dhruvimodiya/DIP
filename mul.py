#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 18:00:28 2023

@author: bmiit202006100110077
"""

# Python program to illustrate
# arithmetic operation of
# bitwise AND of two images
	
# organizing imports
import cv2
import numpy as np

img1 = cv2.imread('3.png')
img2 = cv2.imread('4.png')

dest_xor = cv2.bitwise_xor(img1, img2, mask = None)
  
cv2.imshow('Bitwise XOR', dest_xor)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()

