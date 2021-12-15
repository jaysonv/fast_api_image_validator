import json
from pathlib import Path

import requests

HERE = Path(__file__).parent.absolute()

with open(HERE / "/home/batman/Desktop/fast_api_image_validator/kevin.png", "rb") as fh:
    url = "http://localhost:8000/validate"
    files = {"upload_file": fh}
    # values = {"foo": "hello", "bar": 123, "meta_config": {"prop1": "hello there", "prop2": ["general", "kenobi", 1]}}
    values = {"username" : "bestie", 
    "validators" : ["BlackWhiteThresholdAnalyzer"]}
    resp = requests.post(url, files=files, data={"model": json.dumps(values)})
    print(resp.status_code)
    print(resp.json())