from models.player import Player
from models.turn import Turn
from models.match import Match
from views.turn import Turns


class MatchController:
    def generate_matchs(self, players_list, match_number, tournament_id, turn_id):
        rank_list = Player.get_data_from_players_id(players_list, 'rank')
        order_players_by_rank = sorted(rank_list)

        rank_score_list = Player.get_score_rank_list(order_players_by_rank)
        order_players_by_score = Match.order_score_list(rank_score_list, 1)
        """verifier la liste players_versus pour changer les matchs si besoin"""

        players_list_rank_score_id = Player.add_players_id(order_players_by_score)
        players_name = Player.get_name_data(players_list_rank_score_id, 'name')
        list_id = Player.get_players_id(players_list_rank_score_id)

        order_players_name = Match.order_name(players_name, match_number)
        order_players_id = Match.order_id(list_id, match_number)
        for i in range(len(order_players_id)):
            match_data = Match(tournament_id, turn_id, order_players_id[i][0], order_players_id[i][1],
                               order_players_name[i][0], order_players_name[i][1])
            match_data.get_serialized_match()

    def start_match(self, match_id, current_turn, match_number):
        players_name = Match.get_name(match_id)

        """Display matchs"""
        Turns().display_turns(players_name, current_turn, match_number)