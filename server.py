import io
import os
import sys
import logging
import uvicorn
from PIL import Image

from typing import Type, List, Dict
from fastapi import FastAPI, Form, File,UploadFile, HTTPException
from pydantic import BaseModel, Json, Field

# import your image validator classes
from objects.custom_validator_classes import (
    SimilarityAnalyzer, BlackWhiteThresholdAnalyzer, ValidatorObjectAggregator
)
# import your pydantic models
from objects.pydantic_models import (
    Config,
    ImageFormIn,
    ImageFormOut
)
 
app = FastAPI()

@app.post("/validate", response_model=ImageFormOut)
async def validate(upload_file: UploadFile = File(...), model: Json[ImageFormIn] = Form(...)):
    try:
        filename = os.path.join("downloaded_images", model.username + "_" + upload_file.filename)
        with open(filename, "wb") as fh:
            contents = await upload_file.read()
            fh.write(contents)
            image = Image.open(io.BytesIO(contents)).convert('RGB')
            
            # predicted_class = image_classifier.predict(image, model.threshold)
            aggregator = ValidatorObjectAggregator(*model.validators)
            results = aggregator.processAll(image)
            
            data = {
                "filename": upload_file.filename,
                "username" : model.username, 
                "results" : results
            }
            return ImageFormOut(**data)
    except Exception as error:
        logging.exception(error)
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))
    
