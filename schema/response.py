from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category : str = Field(..., description="Predicted insurance premium category")
    confidence : float = Field(..., description="Confidence of the prediction")
    class_probabilities : Dict[str, float] = Field(..., description="Probabilities for each category")
    
    

    