import io
import os
import sys
import logging
import uvicorn
from PIL import Image

from typing import Type, List, Dict
from fastapi import FastAPI, Form, File,UploadFile, HTTPException, APIRouter
from pydantic import BaseModel, Json, Field

# import your image validator classes
from app.api.objects.custom_validator_classes import (
    SimilarityAnalyzer,
    SquareAnalyzer,
    DominantColorAnalyzer,
    ValidatorObjectAggregator
)

# import your pydantic models
from app.api.objects.pydantic_models import (
    Config,
    ImageFormIn,
    ImageFormOut
)

ROOT_DIR = os.path.dirname(os.path.dirname(__file__))

router = APIRouter()

@router.get("/ping")
async def pong():
    return {"ping": "pong!"}

@router.post("/validate_image", response_model=ImageFormOut)
async def validate(upload_file: UploadFile = File(...), model: Json[ImageFormIn] = Form(...)):
    try:
        filename = os.path.join(ROOT_DIR, "downloaded_images", model.username + "_" + upload_file.filename)
        with open(filename, "wb") as fh:
            contents = await upload_file.read()
            fh.write(contents)
            image = Image.open(io.BytesIO(contents)).convert('RGB')
            
            # predicted_class = image_classifier.predict(image, model.threshold)
            aggregator = ValidatorObjectAggregator(*model.validators)
            results = aggregator.processAll(image)
            
            output_data = {
                "filename": upload_file.filename,
                "username" : model.username, 
                "results" : results
            }
            return ImageFormOut(**output_data)
    except Exception as error:
        logging.exception(error)
        e = sys.exc_info()[1]
        raise HTTPException(status_code=500, detail=str(e))
    