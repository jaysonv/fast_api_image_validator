import json
from pathlib import Path
import requests

HERE = Path(__file__).parent.absolute()

with open(HERE / "/home/batman/Desktop/fast_api_image_validator/downloaded_images/lego.png", "rb") as fh:
    url = "http://localhost:8000/validate"
    files = {"upload_file": fh}
    values = {
        "username" : "user1234", 
        "validators" : ["BlackWhiteThresholdAnalyzer",
        "DominantColorAnalyzer"], # shows will override default
        "config": {"threshold": 0.2} # shows will override default
    }
    resp = requests.post(url, files=files, data={"model": json.dumps(values)})
    print(resp.status_code)
    print(resp.json())