import json
from pathlib import Path
import requests
import cv2
import os
import time
from imutils import paths

# HERE = Path(__file__).parent.absolute()
# print(f'HERE: {HERE}')

def imlist(path):
    return [os.path.join(path, f) for f in os.listdir(path)]

# path to local folder with load test imgs
paths = imlist(os.path.join("api", "load_test_imgs"))


print(paths)
for idx, path in enumerate(paths):
    # if idx <= 3:
    with open(path, "rb") as fh:
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
        
