from tinydb import TinyDB, Query

User = Query()

db = TinyDB("db_player.json")
players_table = db.table("players")


class Player:
    def __init__(self, name, first_name, birthday, gender):  # players table
        self.id = (len(players_table) + 1)
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.gender = gender
        self.rank = (len(TinyDB("db_player.json").table("players")) + 1)
        self.score = 0.0
        self.elo = 0.0

    def get_serialized_player(self):  # insert serialized player
        serialized_player = {
            "id": self.id,
            "name": self.name,
            "first_name": self.first_name,
            "birthday": self.birthday,
            "gender": self.gender,
            "rank": self.rank,
            "score": self.score,
            "elo": self.elo
        }
        players_table.insert(serialized_player)

    def update_players_rank(self):  # update rank based on elo
        pass

    @staticmethod
    def get_players_data():  # get players data for tournament creation
        players = players_table.all()
        players_data = []
        for i in range(len(players_table)):
            list_players = []
            list_players.append(players[i]["id"])
            list_players.append(players[i]["name"])
            list_players.append(players[i]["first_name"])
            list_players.append(players[i]["rank"])
            players_data.append(list_players)
        return players_data

    @staticmethod
    def get_data_from_players_id(players_id, table_information):
        list = []
        for i in range(len(players_id)):
            selected_player = players_table.search(User.id == players_id[i])
            current_choice = selected_player[0][table_information]
            list.append(current_choice)
        return list

    @staticmethod
    def get_data_from_players_rank(players_id, table_information):
        list = []
        for i in range(len(players_id)):
            selected_player = players_table.search(User.rank == players_id[i])
            current_choice = selected_player[0][table_information]
            list.append(current_choice)
        return list
