# fast_api_image_validator

An image validator using FastAPI.

## Preconditions:

- Python 3

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

### Run test

```
pytest app/test.py
```


## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

## POST endpoint

```
http://127.0.0.1:8000/validate
```

## POST to 'http://127.0.0.1:8000/validate' with Curl

```
curl -X 'POST' \
  'http://127.0.0.1:8000/validate' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'upload_file=@docs.png;type=image/png' \
  -F 'model={
  "username": "z1",
  "validators": [
    "BlackWhiteThresholdAnalyzer", "SimilarityAnalyzer"
  ],
  "threshold": 0.1
}'
```

## Example Response

```
{
  "filename": "docs.png",
  "username": "user1234",
  "results": {
    "BlackWhiteThresholdAnalyzer": true,
    "SimilarityAnalyzer": true
  }
}
```


## Example Images
![Example of documented route part 1](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/route_docs1.png)


![Example of documented route part 2](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/route_docs2.png)
