from tinydb import TinyDB

db = TinyDB("db_player.json")
players_table = db.table("players")
players = players_table.all()


class Player:
    def __init__(self, name, first_name, birthday, gender):  # players table
        self.id = (len(TinyDB("db_player.json").table("players")) + 1)
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
