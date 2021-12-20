import json
from pathlib import Path
import requests
import cv2
import os
import time


def imlist(path):
    """
    The function imlist returns all the names of the files in 
    the directory path supplied as argument to the function.
    """
    return [os.path.join(path, f) for f in os.listdir(path)]


if __name__ == "__main__":
    load_test_imgs = imlist(os.path.join("api", "downloaded_images"))

    for file in load_test_imgs:
        print(f'removing {file}')
        os.remove(file)

    # path to folder with load test imgs
    paths = imlist(os.path.join("api", "load_test_imgs"))
    print(paths)


    # start timer
    start = time.perf_counter()

    list_of_dicts = []
    counter = 0
    for idx, path in enumerate(paths):
        with open(path, "rb") as fh:
            url = "http://localhost:8000/api/isvalid/validate_image"
            files = {"upload_file": fh}
            values = {
                "username" : f"user{idx}", 
                "validators" : ["DominantColorAnalyzer", "SquareAnalyzer"],
                "config": {"threshold": 0.2}
            }
            resp = requests.post(url, files=files, data={"model": json.dumps(values)})
            print(resp.status_code)
            print(resp.json())
            list_of_dicts.append(resp.json())
            counter += 1

    # display results
    duration = time.perf_counter() - start
    print(f'total images processed: {counter} in {duration:.1f}seconds')
            
    # print(list_of_dicts[0]["results"])
    
    true_count = 0
    for d in list_of_dicts:
        try:
            if d["results"]["SquareAnalyzer"] == True:
                print("TRUE")
                print(d)
                true_count += 1
        except Exception as e:
            print("invalid")
    print(f"done checking.\n{true_count} are square")