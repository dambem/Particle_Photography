# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 21:54:08 2020

@author: bembe
"""

from PIL import Image, ImageFilter
import numpy as np

im = Image.open('damian3.png') 
pixel_values = list(im.getdata())
print(pixel_values[0])
pix = im.load()

pixels = []

# Get the width and hight of the image for iterating over
for x in range(im.size[0]):
   for y in range(im.size[1]):
       with open('image3.txt', 'a') as myfile:
            myfile.write(str(pix[x,y][0]) + ",")       
