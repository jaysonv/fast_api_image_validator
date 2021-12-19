import json
from pathlib import Path
import requests

HERE = Path(__file__).parent.absolute()

with open(HERE / "/home/batman/Desktop/fast_api_image_validator/docs/route0.png", "rb") as fh:
    url = "http://localhost:8000/api/isvalid/validate_image"
    files = {"upload_file": fh}
    values = {
        "username" : "user1234", 
        "validators" : ["BlackWhiteThresholdAnalyzer"],
        "config": {"threshold": 0.2}
    }
    resp = requests.post(url, files=files, data={"model": json.dumps(values)})
    print(resp.status_code)
    print(resp.json())