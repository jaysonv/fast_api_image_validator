from pydantic import (
    BaseModel, Json, Field
)
from typing import List, Dict


class Config(BaseModel):
    threshold: float = Field(default=.1, description="The dummy threshold value")
    threshold2: float = Field(default=100, description="The second dummy threshold value")

class ImageFormOut(BaseModel):
    filename: str
    username: str
    results: Dict

class ImageFormIn(BaseModel):
    username: str
    validators: List[str] = ["SquareAnalyzer",
    "DominantColorAnalyzer"]
    config: Config
    
    
