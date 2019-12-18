import numpy as np 
import cv2 
import math
import scipy 
from scipy.signal import medfilt

def tone_func (img1, eps1, eps2, eps3, phi):
    #Divides all pixels in the image by the maximum possible intensity in 8 bits which is 255, needed for thresholding
    out_img = img1/255
    #Loops through the dimensions of the image
    for i in range (0, out_img.shape[0]):     
        for j in range (0, out_img.shape[1]):
            #Compares image intensities to each epsilon value, and assigns them a new value depending on how great their intensity is
            #Range between 0 and 0.3
            if out_img[i][j] < eps1:     
                out_img[i][j] = 0.25*np.tanh(phi*(out_img[i][j] - 0)) + 0.5 + 0.25*np.tanh(phi*(out_img[i][j]-eps1))
            #Ranges from 0.3 to 0.4
            elif out_img[i][j] >= eps1 and out_img[i][j] < eps2:
                out_img[i][j] = 1
            #Ranges from o.4 to 0.6
            elif out_img[i][j] >= eps2 and out_img[i][j] < eps3:
                out_img[i][j] = 0.25*np.tanh(phi*(out_img[i][j] - eps2)) + 0.5 + 0.25*np.tanh(phi*(out_img[i][j]-eps3))
            #Ranges from 0.6 to 1(max)
            elif out_img[i][j] >= eps3:
                out_img[i][j] = 1
    #Returns the three tone image and is multiplied by 255 so it can become a grayscale 8 bit image again
    return (out_img * 255)
#Reads input image
image_in = cv2.imread('XDoG_orca.png',0)
#Calls upon threetone function
output_img = tone_func(image_in, 0.3, 0.4, 0.6, 6)
cv2.imwrite("orca_3_tone.png", output_img)
