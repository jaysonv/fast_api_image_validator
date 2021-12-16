# fast_api_image_validator

An image validator using FastAPI.

## Clone the project

```
git clone https://github.com/k-zehnder/fast_api_image_validator
```

## Run local

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn server:app --reload
```

### Run test (*)

```
pytest app/test.py
```


## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

## POST endpoint

```
import json
from pathlib import Path
import requests

HERE = Path(__file__).parent.absolute()

with open(HERE / "/home/batman/Desktop/fast_api_image_validator/kevin.png", "rb") as fh:
    url = "http://localhost:8000/validate"
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
http://127.0.0.1:8000/validate
```

## POST to 'http://127.0.0.1:8000/validate' with Curl

```
curl -X 'POST' \
  'http://127.0.0.1:8000/validate' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'upload_file=@Screenshot from 2021-12-05 07-40-46.png;type=image/png' \
  -F 'model={
  "username": "t1",
  "validators": [
    "SimilarityAnalyzer",
    "BlackWhiteThresholdAnalyzer"
  ],
  "config": {
    "threshold": 0.1
  }
}'
```

## Example Response Body

```
{
  "filename": "Screenshot from 2021-12-05 07-40-46.png",
  "username": "t1",
  "results": {
    "SimilarityAnalyzer": true,
    "BlackWhiteThresholdAnalyzer": true
  }
}
```


## Example Images
![Example of documented route part 1](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/route_docs1.png)

