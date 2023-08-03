#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:03:42 2023

@author: bmiit202006100110077
"""

import cv2
img = cv2.imread('img.jpeg')
cv2.imshow('original img',img)

#  = input("input x value :")
x = 200
y =199

print("current pixel value of image",img[x][y])
print()
print("right pixel :(", x + 1,",",y,") and its value is :",img[x+1][y])
print("right pixel :(", x - 1,",",y,") and its value is :",img[x-1][y])

cv2.waitKey(0)
cv2.destroyAllWindows()