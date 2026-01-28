class Player:
    def __init__(self, raw):
        self.raw = raw

    def kd(self):
        kills = self.raw["estadisticas"]["combate"]["kills"]
        deaths = self.raw["estadisticas"]["combate"]["deaths"]
        return round(kills / max(deaths, 1), 2)

    def headshot_pct(self):
        hs = self.raw["estadisticas"]["precision"]["headshots"]
        imp = self.raw["estadisticas"]["precision"]["impactos"]
        return round((hs / max(imp, 1)) * 100, 2)
    