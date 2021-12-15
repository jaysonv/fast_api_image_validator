import os
import time
import datetime
import cv2
from abc import ABC, abstractmethod
from tqdm import tqdm

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
    
if __name__ == "__main__":
    pass
