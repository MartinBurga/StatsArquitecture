class RiskServiceQuery:
    def __init__(self, repo):
        self.repo = repo

    def get_leaderboard(self):
        return self.repo.get_players_sorted_by_kills()
