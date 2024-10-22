from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    amount: float
    location: str
