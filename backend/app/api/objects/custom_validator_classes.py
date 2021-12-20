import os
import time
import datetime
from abc import ABC, abstractmethod
from tqdm import tqdm
from typing import List, Dict

import cv2
import numpy as np
from PIL import Image

from app.api.objects.utils import get_color_name, get_dominant_color


ROOT_DIR = os.path.dirname(os.path.dirname(__file__))


class ImageValidator(ABC):
    @abstractmethod
    def isValidImage(self, image):
        pass

class SimilarityAnalyzer(ImageValidator):
    def isValidImage(self, image):
        return True
    
class SquareAnalyzer(ImageValidator):
    def isValidImage(self, image):
        return image.width == image.height

class DominantColorAnalyzer(ImageValidator):
    def isValidImage(self, image):
        dominant_color = get_dominant_color(image)
        wanted_color = "purple"
        print(f'get color name {get_color_name(dominant_color)}')
        return get_color_name(dominant_color) == wanted_color

class ValidatorObjectAggregator:
    def __init__(self, *validator_objects: List[object]) -> None:
        self.validators = [obj for obj in validator_objects]
        self.validators_dictionary = {
            "SimilarityAnalyzer" : SimilarityAnalyzer,
            "SquareAnalyzer" : SquareAnalyzer,
            "DominantColorAnalyzer" : DominantColorAnalyzer
        }

    def processAll(self, image):
        results = {}
        for validator_key in self.validators:
            validity_object = self.validators_dictionary[validator_key]()
            results[f"{validator_key}"] = validity_object.isValidImage(image) 
        return results
         
    def __str__(self):
        return str(self.validators)

     
if __name__ == "__main__":
    val_objects = ["SimilarityAnalyzer", "DominantColorAnalyzer"]
    aggregator = ValidatorObjectAggregator(*val_objects)
    print(aggregator)
    
    # instantiate dominant color validator
    dom_analyzer = DominantColorAnalyzer()

    # specify path to image to test on
    file = os.path.join(ROOT_DIR, "downloaded_images", "lego.png")
    print(file)
    print(dom_analyzer.isValidImage(file))