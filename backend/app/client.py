import json
from pathlib import Path
import requests
import cv2
import os
import time
from imutils import paths

HERE = Path(__file__).parent.absolute()

def imlist(path):
    """
    The function imlist returns all the names of the files in 
    the directory path supplied as argument to the function.
    """
    return [os.path.join(path, f) for f in os.listdir(path)]

paths = imlist("/home/batman/Desktop/fast_api_image_validator/docs")

for idx, path in enumerate(paths):
    # if idx <= 3:
    with open(HERE / f"{path}", "rb") as fh:
        url = "http://localhost:8000/api/isvalid/validate_image"
        files = {"upload_file": fh}
        values = {
            "username" : f"user{idx}", 
            "validators" : ["BlackWhiteThresholdAnalyzer"],
            "config": {"threshold": 0.2}
        }
        resp = requests.post(url, files=files, data={"model": json.dumps(values)})
        print(resp.status_code)
        print(resp.json())
        
