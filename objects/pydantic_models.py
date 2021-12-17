from pydantic import (
    BaseModel, Json, Field
)
from typing import List, Dict


class Config(BaseModel):
    threshold: float = Field(default=.1, description="The threshold")

class ImageFormOut(BaseModel):
    filename: str
    username: str
    results: Dict

class ImageFormIn(BaseModel):
    username: str
    validators: List[str] = ["SimilarityAnalyzer", "BlackWhiteThresholdAnalyzer"]
    config: Config
    
    
