import random
from Classes import AnalysisResponse
from Classes import AnalysisRequest

def analyze_transaction(request):
    return AnalysisResponse.AnalysisResponse("Analise com sucesso", random.choice([True, False]))

