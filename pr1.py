#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 17:45:48 2023

@author: bmiit202006100110077
"""

import cv2
import matplotlib as plt

image = cv2.imread('img.jpeg')
height, width = image.shape

image[0][5]=225
cv2.imshow('image',image)

cv2.waitKey(0)

cv2.destroyAllWindows()
