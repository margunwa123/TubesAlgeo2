"""
eehehehehe
"""
import numpy as np
#import cv2
from matplotlib import pyplot as plt

img = cv2.imread("test.jpg",0)

# Initiate STAR detector
orb = cv2.ORB_create()

# compute the descriptors with ORB
kp, des = orb.detectAndCompute(img, None)

# draw only keypoints location,not size and orientation
img = cv2.drawKeypoints(img, kp, None)
cv2.imshow("Image", img)
cv2.waitKey(0)
