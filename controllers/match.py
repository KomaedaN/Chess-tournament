from models.player import Player
from models.turn import Turn
from models.match import Match


class MatchController:
    def fist_turn_match(self, players_list, match_number, tournament_id, turn_id):
        rank_list = Player.get_data_from_players_id(players_list, 'rank')
        order_players_by_rank = Match.order_rank_list(rank_list)

        players_name = Player.get_data_from_players_rank(rank_list, 'name')
        update_players_name = Match.first_match_order_rank(players_name, match_number)
        update_players_id = Match.first_match_order_rank(order_players_by_rank, match_number)
        for i in range(len(update_players_id)):
            match_data = Match(tournament_id, turn_id, update_players_id[i][0], update_players_id[i][1], update_players_name[i][0], update_players_name[i][1])
            match_data.get_serialized_match()

        #  update_score*

    def all_other_match(self):
        pass