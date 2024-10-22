import random

class AnalysisResponse():
    status: str
    statusCode: str
    accepted: bool
    reason: str
    score: float

    def __init__(self, status, result):
        self.status = status
        self.statusCode = self.GetStatusCode(result)
        self.reason = self.GetReason(result)
        self.accepted = result
        self.score = self.GetScore(result)

        
    @staticmethod
    def GetStatusCode(result):
        if result is True:
            return "000"
        else:
            return "999"

    @staticmethod
    def GetScore(result):
        if result is True:
            return round( (random.uniform(0,0.5)), 2)
        else:
            return round( (random.uniform(0.5,1)), 2)
            
    @staticmethod
    def GetReason(result):
        if result is True:
            return "Compra válida"
        else:
            return random.choice(reason_list)

reason_list = [
    'Localização fora da rota',
    'Repetição de valores',
    'Horário fora do esperado',
    'Comprou 600 baldes de pipoca no Cinema Chiquinho Scarpa',
    'Falso positivo']