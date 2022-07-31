from models.tournament import Tournament
from views.tournament import NewTournament


class TurnController:
    def turn(self):
        tournaments_data = Tournament.get_tournaments_data()
        NewTournament().display_tournament(tournaments_data)
        """JEN SUIS LA MEC"""
