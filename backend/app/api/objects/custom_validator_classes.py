import os
import time
import datetime
from abc import ABC, abstractmethod
from tqdm import tqdm
from typing import List, Dict

import cv2
import numpy as np
# from skimage import io


# ROOT_DIR = "/home/batman/Desktop/fast_api_image_validator" # This is your Project Root
ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


class ImageValidator(ABC):
    @abstractmethod
    def isValidImage(self, image):
        pass

class SimilarityAnalyzer(ImageValidator):
    def isValidImage(self, image):
        return True
    
class BlackWhiteThresholdAnalyzer(ImageValidator):
    def isValidImage(self, image):
        return True

class DominantColorAnalyzer(ImageValidator):
    def isValidImage(self, image):
        # img = cv2.imread(image)
        # print(f'type image: {type(image)}')
        
        # get dominant colors
        #palette = get_dominant_colors(image)
        return False

class ValidatorObjectAggregator:
    def __init__(self, *validator_objects: List[object]) -> None:
        self.validators = [obj for obj in validator_objects]
        self.validators_dictionary = {
            "SimilarityAnalyzer" : SimilarityAnalyzer,
            "BlackWhiteThresholdAnalyzer" : BlackWhiteThresholdAnalyzer,
            "DominantColorAnalyzer" : DominantColorAnalyzer
        }

    def processAll(self, image):
        results = {}
        # TODO: for val_key, settings in self.validators:
        for validator_key in self.validators:
            validity_object = self.validators_dictionary[validator_key]()
            results[f"{validator_key}"] = validity_object.isValidImage(image) 
        return results
         
    def __str__(self):
        return str(self.validators)
    
    
def get_dominant_colors(image_array):
    pass
"""    # convert from pillow to cv2 to play nice with skimage
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
    return dominant""" 
     
if __name__ == "__main__":
    val_objects = ["SimilarityAnalyzer", "BlackWhiteThresholdAnalyzer", "DominantColorAnalyzer"]
    aggregator = ValidatorObjectAggregator(*val_objects)
    print(aggregator)
    
    # instantiate dominant color validator
    dom_analyzer = DominantColorAnalyzer()

    # specify path to image to test on
    file = os.path.join(ROOT_DIR, "downloaded_images", "lego.png")
    print(file)
    print(dom_analyzer.isValidImage(file))