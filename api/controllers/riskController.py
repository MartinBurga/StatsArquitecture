from domain.services.riskCalculator import RiskCalculator

calculator = RiskCalculator()

def calculate_risk(jugador):
    risk = calculator.calculate(
        jugador["kda"],
        jugador["headshots"]
    )
    jugador["risk_score"] = risk
    return jugador
