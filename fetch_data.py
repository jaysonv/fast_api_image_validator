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


from objects.googleImageScraper import GoogleImageScraper


if __name__ == "__main__":
    # hard code configs
    config = {
        "output_path" : "/home/batman/Desktop/fast_api_image_validator/downloaded_images",
        "chrome_driver_path" : "/home/batman/Desktop/fast_api_image_validator/chromedriver",
        "headless" : True
    }

    # start timer
    start = time.perf_counter()
    
    # instantiate google images scraper object w/ config dict values
    scraper = GoogleImageScraper(**config)
    
    # fetch and download images to output path
    img_urls = scraper.fetch_image_urls("boeing 747", 10, 1)
    for url in img_urls:
        scraper.persist_one_image(url)
    
    # fetch images from output path
    downloaded_imgs = scraper.load_images_from_folder()
    print(type(downloaded_imgs[0]))
    print(len(downloaded_imgs))
    
    # display results
    default_duration = time.perf_counter() - start
    print(f'NO RAY: {default_duration * 1000:.1f}ms')
    
