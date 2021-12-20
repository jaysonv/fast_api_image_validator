# fast_api_image_validator
![Demo speed](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/demo_speed.png)

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
http://0.0.0.0:8000/docs
```

## POST to endpoint 'http://0.0.0.0:8000/api/isvalid/validate_image' using requests module

```
import json
from pathlib import Path
import requests

image_path = "docs/route0.png"
with open(image_path, "rb") as fh:
    url = "http://localhost:8000/api/isvalid/validate_image"
    files = {"upload_file": fh}
    values = {
        "username" : "user1234", 
        "validators" : ["SquareAnalyzer"],
        "config": {"threshold": 0.2}
    }
    resp = requests.post(url, files=files, data={"model": json.dumps(values)})
    print(resp.status_code)
    print(resp.json())
```

## POST to endpoint 'http://0.0.0.0:8000/api/isvalid/validate_image' using Curl

```
curl -X 'POST' \
  'http://0.0.0.0:8000/api/isvalid/validate_image' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'upload_file=@square.jpg;type=image/jpeg' \
  -F 'model={
  "username": "test_user",
  "validators": [
    "SquareAnalyzer",
    "DominantColorAnalyzer"
  ],
  "config": {
    "threshold": 0.1,
    "threshold2": 100
  }
}'
```

## Example Response Body

```	
{
  "filename": "square.jpg",
  "username": "test_user",
  "results": {
    "SquareAnalyzer": true,
    "DominantColorAnalyzer": false
  }
}
```

## Example Images
![Example of documented route part 1](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/route0.png)

![Example of documented route part 2](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/route2.png)
