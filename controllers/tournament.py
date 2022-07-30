from tinydb import TinyDB
from views.tournament import NewTournament
from models.tournament import Tournament


class TournamentController:
    def create_tournament(self):
        """get all entries"""
        name = NewTournament().name_entrie()
        place = NewTournament().place_entrie()
        date = NewTournament().date_entrie()
        description = NewTournament().description_entrie()
        time_control = NewTournament().time_control_entrie()
        selected_player_id = NewTournament().selected_players_id_entrie()
        nbr_of_rounds = NewTournament().number_of_rounds_entrie()

        """Serialized tournament"""
        tournament_entries = Tournament(name, place, date, description, time_control, selected_player_id, nbr_of_rounds)
        tournament_entries.get_serialized_tournament()
