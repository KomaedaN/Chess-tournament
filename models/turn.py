from tinydb import TinyDB, Query

User = Query()

db = TinyDB("db_turn.json")
turns_table = db.table("turns")


class Turn:
    def __init__(self, tournament_id, selected_players_id, match_id=[], number_of_turn=1):  # turns table
        self.id = (len(turns_table) + 1)
        turn = turns_table.search(User.tournament_id == tournament_id)
        self.current_turn = (len(turn) + 1)
        self.tournament_id = tournament_id
        self.selected_players_id = selected_players_id
        self.match_id = match_id
        self.number_of_turn = number_of_turn

    def get_serialized_turn(self):  # insert serialized player
        serialized_turn = {
            "id": self.id,
            "current_turn": self.current_turn,
            "tournament_id": self.tournament_id,
            "selected_players_id": self.selected_players_id,
            "match_id": self.match_id,
            "number_of_turn": self.number_of_turn
        }
        turns_table.insert(serialized_turn)

    @staticmethod
    def get_current_turn(current_tournament):
        selected_tournament = turns_table.search(User.tournament_id == current_tournament)
        current_turn = selected_tournament[0]['number_of_turn']
        return current_turn

    @staticmethod
    def get_id_from_current_turn(current_tournament, current_turn):
        selected_tournament = turns_table.search(User.tournament_id == current_tournament)
        for i in range(len(selected_tournament)):
            if int(selected_tournament[i]['current_turn']) == current_turn:
                return selected_tournament[i]['id']

    @staticmethod
    def update_match_id(match_id_per_turn, turn_id):
        turns_table.update({'match_id': match_id_per_turn}, User.id == turn_id)
