import os
import time
import datetime
from abc import ABC, abstractmethod
from tqdm import tqdm
from typing import List, Dict

import cv2
import numpy as np
from skimage import io

from objects.utils import get_dominant_colors

ROOT_DIR = "/home/batman/Desktop/fast_api_image_validator" # This is your Project Root


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
        palette = get_dominant_colors(image)
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
    
# if __name__ == "__main__":
#     val_objects = ["SimilarityAnalyzer", "BlackWhiteThresholdAnalyzer", "DominantColorAnalyzer"]
#     aggregator = ValidatorObjectAggregator(*val_objects)
#     print(aggregator)
    
#     # instantiate dominant color validator
#     dom_analyzer = DominantColorAnalyzer()

#     # specify path to image to test on
#     file = os.path.join(ROOT_DIR, "downloaded_images", "lego.png")
#     print(file)
#     print(dom_analyzer.isValidImage(file))