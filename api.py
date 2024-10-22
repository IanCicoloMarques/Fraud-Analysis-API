from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import random
from Classes import AnalysisResponse
from Classes import AnalysisRequest
from Services import FraudAnalysisServiceMock

api = FastAPI()


@api.post("/credit/analysis")
async def CreditAnalyssisEndpoint(request: AnalysisRequest.AnalysisRequest):
    
    fraudAnalysis = FraudAnalysisServiceMock.analyze_transaction(request)

    response = jsonable_encoder(fraudAnalysis)
    return JSONResponse(content=response) 