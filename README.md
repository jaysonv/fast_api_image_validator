# fast_api_image_validator

An image validator using FastAPI.

## Clone the project

```
git clone https://github.com/k-zehnder/fast_api_image_validator
```

## Run with Docker
```
cd fast_api_image_validator
sudo docker-compose up -d --build
sudo docker-compose up
```

## API documentation (provided by Swagger UI)
```
http://127.0.0.1:8000/docs
```

## POST to endpoint 'http://127.0.0.1:8000/validate' using requests module

```
import json
from pathlib import Path
import requests

HERE = Path(__file__).parent.absolute()

with open(HERE / "/home/batman/Desktop/fast_api_image_validator/docs/route0.png", "rb") as fh:
    url = "http://localhost:8000/api/isvalid"
    files = {"upload_file": fh}
    values = {
        "username" : "user1234", 
        "validators" : ["BlackWhiteThresholdAnalyzer"],
        "config": {"threshold": 0.2}
    }
    resp = requests.post(url, files=files, data={"model": json.dumps(values)})
    print(resp.status_code)
    print(resp.json())
```
```
http://127.0.0.1:8000/api/isvalid/validate_image
```

## POST to endpoint 'http://127.0.0.1:8000/api/isvalid/validate_image' using Curl

```
curl -X 'POST' \
  'http://0.0.0.0:8000/api/isvalid/validate' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'upload_file=@docs.png;type=image/png' \
  -F 'model={
  "username": "kevin",
  "validators": [
    "SimilarityAnalyzer",
    "DominantColorAnalyzer"
  ],
  "config": {
    "threshold": 0.1,
    "threshold2": 200
  }
}'
```

## Example Response Body

```	
{
  "filename": "docs.png",
  "username": "kevin",
  "results": {
    "SimilarityAnalyzer": true,
    "DominantColorAnalyzer": false
  }
}
```

## Example Images
![Example of documented route part 1](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/route0.png)

![Example of documented route part 2](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/route2.png)

![Demo speed](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/demo_speed.png)
