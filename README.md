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
uvicorn app.main:app --reload
```

### Run test

```
pytest app/test.py
```


## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

### Run server

```
uvicorn server:app --reload
```

## Validate endpoint

```
http://127.0.0.1:8000/validate
```



![Example of documented route part 1](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/route_docs1.png)


![Example of documented route part 2](https://github.com/k-zehnder/fast_api_image_validator/blob/main/docs/route_docs2.png)
