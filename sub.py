#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 17:58:48 2023

@author: bmiit202006100110077
"""


# organizing imports
import cv2
import numpy as np
	
# path to input images are specified and
# images are loaded with imread command
image1 = cv2.imread('1.jpg')
image2 = cv2.imread('2.jpg')

# cv2.subtract is applied over the
# image inputs with applied parameters
sub = cv2.subtract(image1, image2)

# the window showing output image
# with the subtracted image
cv2.imshow('Subtracted Image', sub)

# De-allocate any associated memory usage
if cv2.waitKey(0) & 0xff == 27:
	cv2.destroyAllWindows()
