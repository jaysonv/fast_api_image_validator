import cv2
import numpy as np
from skimage import io

def get_dominant_colors(image_array):
    # convert from pillow to cv2 to play nice with skimage
    img = np.asarray(image_array)
    
    # calculate the mean of each chromatic channel
    average = img.mean(axis=0).mean(axis=0)
    
    # next, apply k-means clustering to create a palette with the most representative colors in the image. 
    pixels = np.float32(img.reshape(-1, 3))
    
    # In this toy example n_colors was set to 5.
    n_colors = 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
    flags = cv2.KMEANS_RANDOM_CENTERS

    # dominant colour is the palette colour which occurs most frequently on the quantized image:
    _, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
    _, counts = np.unique(labels, return_counts=True)
    
    dominant = palette[np.argmax(counts)]
    print(f'dominant: {dominant}')
    # return dominant [R, G, B] [179, 27, 2]
    # for lego image
    return dominant