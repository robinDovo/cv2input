#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:04:34 2020

@author: huc
"""

import cv2

img = cv2.imread('lena.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwritw('list3.jpg',gray)
