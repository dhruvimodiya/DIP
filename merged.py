#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 18:40:58 2023

@author: bmiit202006100110077
"""

from PIL import Image

image1 = Image.open('img.jpeg')
image1.show()
image2 = Image.open('py.jpeg')
image2.show()

image1 = image1.resize((426, 240))
image1_size = image1.size
image2_size = image2.size
new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
new_image.paste(image1,(0,0))
new_image.paste(image2,(image1_size[0],0))
new_image.save("merged.jpeg","JPEG")
new_image.show()