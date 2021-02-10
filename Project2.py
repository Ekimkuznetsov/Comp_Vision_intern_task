import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

next_image = input('File name: ')

#Use Canny function to detect edges 
def edge_detection(image):
    edges_detected = cv2.Canny(image, 100, 200)
    images = [image, edges_detected]
    location = [121,122]
    for loc, edge_image in zip(location, images):
        plt.subplot(loc)
    plt.imshow(edge_image, cmap = 'gray')
    cv2.imwrite('edge_detected.png', edges_detected)
    plt.savefig('edge_plot.png')
    #plt.show()

#Extremums detection
def extremum_detection(img):
    img1 = mpimg.imread('edge_detected.png') #To array
    zi = np.argwhere(img1 != 0)
    zi = zi.T
    ymin = min(zi[0]) - 1
    ymax = max(zi[0]) + 1
    xmin = min(zi[1]) - 1
    xmax = max(zi[1]) + 1
    #Back to RGB
    backtorgb = cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
    #Rectangle around area of interest
    final_img = cv2.rectangle(backtorgb, (xmin, ymin), (xmax, ymax), (0, 0, 255), thickness = 2)
    #Saving image
    cv2.imwrite('final.png', final_img)
    coordinates = [xmin + 1, xmax - 1, ymin + 1, ymax - 1]
    result = dict([('file', next_image), ('coord', coordinates)])
    print(result)

#Пробовал сделать перебор изображений, но не хватает времени разобраться. Проблема с осями в 'subplot'
#def list_files(dir_path):
    #files_and_folders = [
      #os.path.abspath(os.path.join(dir_path,file_or_folder)) for file_or_folder in os.listdir(dir_path)
    #]
    #for file in files_and_folders:
        #if os.path.isfile(file):
            #img = cv2.imread(file, 0)
            #edge_detection(img)
            #extremum_detection(img)

img = cv2.imread(next_image, 0)
edge_detection(img)
extremum_detection(img)


