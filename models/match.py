from tinydb import TinyDB, Query

User = Query()

db = TinyDB("db_match.json")
match_table = db.table("match")


class Match:
    def __init__(self, tournament_id, turn_id, player_1_id, player_2_id, player_1_name, player_2_name,
                 player_1_result=0.0,
                 player_2_result=0.0):
        self.id = (len(match_table) + 1)
        match = match_table.search(User.tournament_id == tournament_id)
        self.current_match = (len(match) + 1)
        self.tournament_id = tournament_id
        self.turn_id = turn_id
        self.player_1_id = player_1_id
        self.player_2_id = player_2_id
        self.player_1_name = player_1_name
        self.player_2_name = player_2_name
        self.player_1_result = player_1_result
        self.player_2_result = player_2_result

    def get_serialized_match(self):  # insert serialized player
        serialized_match = {
            "id": self.id,
            "current_match": self.current_match,
            "tournament_id": self.tournament_id,
            "turn_id": self.turn_id,
            "player_1_id": self.player_1_id,
            "player_2_id": self.player_2_id,
            "player_1_name": self.player_1_name,
            "player_2_name": self.player_2_name,
            "player_1_result": self.player_1_result,
            "player_2_result": self.player_2_result
        }
        match_table.insert(serialized_match)

    @staticmethod
    def order_score_list(players, index):
        for o in range(1, len(players)):
            key = players[o]
            j = o - 1
            while j >= 0 and key[index] < players[j][index]:
                players[j + 1] = players[j]
                j -= 1
            players[j + 1] = key
        return players

    @staticmethod
    def order_name(players_data, match_number):
        players_number = len(players_data)
        first_half_players = players_data[:players_number // match_number]
        second_half_players = players_data[players_number // match_number:]
        return first_half_players, second_half_players

    @staticmethod
    def order_id(players_data, match_number):
        players_number = len(players_data)
        first_half_players = players_data[:players_number // match_number]
        second_half_players = players_data[players_number // match_number:]
        return first_half_players, second_half_players

    @staticmethod
    def get_match_id_per_turn(current_turn_id):
        match_table.all()
        match = match_table.search(User.turn_id == current_turn_id)
        match_id = []
        for i in range(len(match)):
            current_match_id = match[i]['id']
            match_id.append(current_match_id)
        return match_id

    @staticmethod
    def get_name(data):
        name_list = []
        for i in range(len(data)):
            group_list = []
            current_match = match_table.search(User.id == data[i])
            player_1 = current_match[0]['player_1_name']
            player_2 = current_match[0]['player_2_name']
            group_list.append(player_1)
            group_list.append(player_2)
            name_list.append(group_list)
        return name_list

    @staticmethod
    def get_turn(data):
        id = data[0]
        current_match = match_table.search(User.id == id)
        current_turn = current_match[0]['current_match']
        return current_match

    @staticmethod
    def verify_tournament_id(id):
        match = match_table.search(User.tournament_id == id)
        if len(match) <= 0:
            input("Ce tournoi n'a pas encore commencé")
        else:
            list = []
            for i in range(len(match)):
                reset_list = []
                current_match = match[i]['current_match']
                player_1 = match[i]['player_1_name']
                player_1_result = match[i]['player_1_result']
                player_2 = match[i]['player_2_name']
                player_2_result = match[i]['player_2_result']
                reset_list.append(current_match)
                reset_list.append(player_1)
                reset_list.append(player_1_result)
                reset_list.append(player_2)
                reset_list.append(player_2_result)
                list.append(reset_list)
            return list


    @staticmethod
    def update_players_score(player_name, player_result, match_id, index):
        match = match_table.search(User.id == match_id)
        match_score = match[0][index] + player_result
        match_table.update({index: match_score}, User.id == match_id)
