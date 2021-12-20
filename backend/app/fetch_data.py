import os
from abc import ABC, abstractmethod
from typing import List, Dict

import cv2
import time
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm
import requests

from api.objects.googleImageScraper import GoogleImageScraper

def imlist(path):
    """
    The function imlist returns all the names of the files in 
    the directory path supplied as argument to the function.
    """
    return [os.path.join(path, f) for f in os.listdir(path)]


if __name__ == "__main__":
    # assign paths
    output_path = os.path.join("api", "load_test_imgs")
    chrome_driver_path = os.path.join("api", "chromedriver")
    
    # remove images if exist
    load_test_imgs_paths = imlist(output_path)
    for file in load_test_imgs_paths:
        print(f'removing {file}')
        os.remove(file)
    
    # dict to instantiate GoogleImageSceaper object with
    config = {
        "output_path" : output_path,
        "chrome_driver_path" : chrome_driver_path,
        "headless" : True
    }

    # start timer
    start = time.perf_counter()
    
    # instantiate GoogleImageScraper
    scraper = GoogleImageScraper(**config)
    
    # fetch and download images to output path
    img_urls = scraper.fetch_image_urls("boeing", 5, 1)
    for url in img_urls:
        scraper.persist_one_image(url)
    
    # fetch images from output path
    downloaded_imgs = scraper.load_images_from_output_path()
    print(type(downloaded_imgs[0]))
    print(len(downloaded_imgs))
    
    # display results
    default_duration = time.perf_counter() - start
    print(f'scraped {len(downloaded_imgs)} images in {default_duration:.1f}   seconds')
    