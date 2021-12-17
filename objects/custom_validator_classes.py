import os
import time
import datetime
import cv2
from abc import ABC, abstractmethod
from tqdm import tqdm
from typing import List, Dict


class ImageValidator(ABC):
    @abstractmethod
    def isValidImage(self):
        pass

class SimilarityAnalyzer(ImageValidator):
    def isValidImage(self, image):
        return True
    
class BlackWhiteThresholdAnalyzer(ImageValidator):
    def isValidImage(self, image):
        return True

class ValidatorObjectAggregator:
    def __init__(self, *validator_objects: List[object]) -> None:
        self.validators = [obj for obj in validator_objects]
        self.validators_dictionary = {
            "SimilarityAnalyzer" : SimilarityAnalyzer,
            "BlackWhiteThresholdAnalyzer" : BlackWhiteThresholdAnalyzer
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
    val_objects = ["SimilarityAnalyzer", "BlackWhiteThresholdAnalyzer"]
    aggregator = ValidatorObjectAggregator(*val_objects)
    print(aggregator)
