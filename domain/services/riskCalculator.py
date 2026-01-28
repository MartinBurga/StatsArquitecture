class RiskCalculator:

    def calculate(self, kda, headshots):
        risk = 0

        if kda > 3:
            risk += 40
        if headshots > 70:
            risk += 60

        return min(risk, 100)
    
    
