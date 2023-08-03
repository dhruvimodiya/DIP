#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 17:27:38 2023

@author: bmiit202006100110077
"""

import numpy as npy
import matplotlib.image as img
from statistics import mean
m = img.imread("img.jpeg")
w, h = m.shape[:2]
newImage = npy.zeros([w,h,4])
print(w)
print(h)

        