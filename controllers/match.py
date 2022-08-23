from models.player import Player
from models.match import Match
from views.turn import Turns


class MatchController:
    def generate_matchs(self, players_list, match_number, tournament_id, turn_id, current_turn):
        rank_list = Player.get_data_from_players_id(players_list, 'rank')
        order_players_by_rank = sorted(rank_list)

        """First turn based on players rank"""

        rank_score_list = Player.get_score_rank_list(order_players_by_rank)
        order_players_by_score = Match.order_score_list(rank_score_list, 1)

        players_list_rank_score_id = Player.add_players_id(order_players_by_score)

        #  players_name = Player.get_name_data(players_list_rank_score_id, 'name')
        list_id = Player.get_players_id(players_list_rank_score_id)

        order_players_id = Match.assign_match(list_id, match_number, current_turn)

        order_players_name = Player.order_name(order_players_id)

        Player.update_player_versus(order_players_id)

        for i in range(len(order_players_id)):
            match_data = Match(tournament_id, turn_id, order_players_id[i][0], order_players_id[i][1],
                               order_players_name[i][0], order_players_name[i][1])
            match_data.get_serialized_match()

    def start_match(self, match_id, current_turn, match_number):
        players_name = Match.get_name(match_id)

        """Display matchs"""
        Turns().display_turns(players_name, current_turn, match_number, match_id)
