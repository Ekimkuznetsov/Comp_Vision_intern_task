import matplotlib.pyplot as plt #For plotting of the pic
import matplotlib.image as mpimg #For reading of the pic
import numpy as np
import matplotlib
import cv2
img1 = mpimg.imread('SR1.png')
lum_img1 = img1[:,:,0] #Dimencion change to gray
img2 = mpimg.imread('SR12.png',)
lum_img2 = img2[:,:,0]

imgplot = plt.imshow(img1)
imgplot = plt.imshow(img2)
#plt.show()

array1 = np.array(lum_img1) #Creating 2D array of pixels
array2 = np.array(lum_img2)
print(array1.shape)
print(array2.shape)
#print(array1)
#print(array2)

#Zero padding
mask1 = np.zeros((98, 126))
mask2 = np.zeros((98, 126))
mask3 = np.zeros((98, 126))
x1_offset = 1
y1_offset = 1
mask1[x1_offset:array1.shape[0] + x1_offset, y1_offset:array1.shape[1] + y1_offset] = array1
print('Mask1:', mask1.shape)
x2_offset = 6
y2_offset = 1
mask2[x2_offset:array2.shape[0] + x2_offset, y2_offset:array2.shape[1] + y2_offset] = array2
print('Mask2:', mask2.shape)

#Correlation
x_range = range(1, 98)
y_range = range(1, 126)
def correlation(range1, range2):
    for r in x_range:
        for c in y_range:
            r_start = r - 1 #Parameters for array slicing row and column
            r_end = r + 2
            c_start = c - 1
            c_end = c + 2
            cell1 = mask1[r_start: r_end, c_start: c_end] #Correlation matrix 3x3
            cell2 = mask2[r_start: r_end, c_start: c_end]
            cor_pixel = (cell1 * cell2).sum() / 9
            mask3[r, c] = cor_pixel
    return(mask3)
correlation(x_range, y_range)
imgplot = plt.imshow(mask3)
plt.show()




matplotlib.image.imsave('mask3.png', mask3)




