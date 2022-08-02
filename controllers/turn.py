from models.tournament import Tournament
from models.player import Player
from models.turn import Turn
from models.match import Match

from controllers.match import MatchController
from views.tournament import NewTournament
from views.turn import Turns


class TurnController:
    def turn(self):
        """get data from tournament"""
        tournaments_id = Tournament.get_tournaments_id()
        tournaments_data = Tournament.get_tournaments_data()

        """get all data from turn and match"""
        NewTournament().display_tournament(tournaments_data)  # display tournaments
        selected_tournament_id = NewTournament().selected_tournament(tournaments_id)  # select tournament
        selected_players_id = Tournament.get_selected_players_id(selected_tournament_id)  # get players id

        """Serialized turn"""
        turn_data = Turn(selected_tournament_id, selected_players_id)
        turn_data.get_serialized_turn()

        players_name = Player.get_data_from_players_id(selected_players_id, 'name')  # get players name
        current_turn = Turn.get_current_turn(selected_tournament_id)
        turn_id = Turn.get_id_from_current_turn(selected_tournament_id, current_turn)
        match_per_turn = int(len(selected_players_id) / 2)
        MatchController().fist_turn_match(selected_players_id, match_per_turn, selected_tournament_id, turn_id)
        get_match_id_per_turn = Match.get_match_id_per_turn(turn_id)
        Turn.update_match_id(get_match_id_per_turn, turn_id)
        """Display turns"""
        Turns().display_turns(len(selected_players_id), players_name, players_name, current_turn, match_per_turn)
