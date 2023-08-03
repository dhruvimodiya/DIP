#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:15:27 2023

@author: bmiit202006100110077
"""

from PIL import Image
  
Original_Image = Image.open("py.jpeg")
  
#rotated_image1 = Original_Image.rotate(180)
  
rotated_image2 = Original_Image.transpose(Image.FLIP_LEFT_RIGHT)
  
#rotated_image3 = Original_Image.rotate(60)

#rotated_image4 = Original_Image.rotate(35)
  
#rotated_image1.show()
rotated_image2.show()
#rotated_image3.show()
#rotated_image4.show()