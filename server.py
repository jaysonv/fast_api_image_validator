from fastapi import FastAPI, Form, File, UploadFile, HTTPException
import uvicorn
from pydantic import BaseModel, Json, Field
from typing import Type, List
import cv2
import logging

from PIL import Image
import io
import sys
import logging


from tmp_custom_validator_classes import SimilarityAnalyzer, BlackWhiteThresholdAnalyzer

validators_dictionary = {
    "SimilarityAnalyzer" : SimilarityAnalyzer,
    "BlackWhiteThresholdAnalyzer" : BlackWhiteThresholdAnalyzer
}

class TestModelResponse(BaseModel):
    pass

class TestModel(BaseModel):
    username: str
    validators: List[str]
    threshold: float = Field(default=.1, description="The threshold")
    

app = FastAPI()

@app.post("/validate")
async def foo(upload_file: UploadFile = File(...), model: Json[TestModel] = Form(...)):
    filename = model.username + ".png"
    try:
        with open(filename, "wb") as fh:
            contents = await upload_file.read()
            image = Image.open(io.BytesIO(contents)).convert('RGB')
            fh.write(contents)
            
            # predicted_class = image_classifier.predict(image)
            validator_key = model.validators[0]
            validity_object = validators_dictionary[validator_key]()
            isValidImage = validity_object.isValidImage(image)
            
            # log to console
            #logging.info(f"Is valid?: {isValid}")
            
            # return json object to client (aka response.conent)
            return {
                "filename": upload_file.filename, 
                "contentype": upload_file.content_type,
                "isValidImage" : isValidImage
            }
    except Exception as error:
        logging.exception(error)
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))
    
