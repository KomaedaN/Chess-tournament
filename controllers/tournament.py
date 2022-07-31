from tinydb import TinyDB
from views.tournament import NewTournament
from views.player import CreatePlayer
from models.tournament import Tournament
from models.player import Player


class TournamentController:
    def create_tournament(self):
        players_data = Player.get_players_data()
        """get all entries"""
        name = NewTournament().name_entrie()
        place = NewTournament().place_entrie()
        date = NewTournament().date_entrie()
        description = NewTournament().description_entrie()
        time_control = NewTournament().time_control_entrie()
        display_players = CreatePlayer().display_players(players_data)  # display players before selection
        selected_player_id = NewTournament().selected_players_id_entrie(players_data)
        maximum_rounds = len(selected_player_id)  # maximum rounds = number of selected players
        nbr_of_rounds = NewTournament().number_of_rounds_entrie(maximum_rounds)

        """Serialized tournament"""
        tournament_entries = Tournament(name, place, date, description, time_control, selected_player_id, nbr_of_rounds)
        tournament_entries.get_serialized_tournament()
