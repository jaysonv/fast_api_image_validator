from starlette.testclient import TestClient

from app.api.server import app
import os
import cv2
import requests
import json

client = TestClient(app)

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def test_get_validators():
    response = client.get("/api/isvalid/validators")
    assert response.status_code == 200
    assert response.json() == {
        "validators": [
            "SimilarityAnalyzer",
            "SquareAnalyzer",
            "DominantColorAnalyzer"
            ]
    }

    
def test_post_submit_image():
    image_path = "/home/batman/Desktop/fast_api_image_validator/docs/square.jpg"
    with open(image_path, "rb") as fh:
        files = {"upload_file": fh}
        values = {
        "username" : "test_user", 
        "validators" : ["SquareAnalyzer"],
        "config": {"threshold": 0.2}
        }
        
        response = client.post("api/isvalid/validate_image", files=files, data={"model": json.dumps(values)})
        test_response_payload = {
            "filename": "square.jpg",
            "username": "test_user",
            "results": {
                "SquareAnalyzer": True
            }
        }

        assert response.status_code == 200
        assert response.json() == test_response_payload