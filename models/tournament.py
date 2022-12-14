from tinydb import TinyDB, Query

User = Query()

db = TinyDB("db_tournament.json")
tournaments_table = db.table("tournaments")


class Tournament:
    def __init__(self, name, place, date, description="", time_control="", selected_players=[], number_of_rounds=4):
        self.id = (len(tournaments_table) + 1)
        self.name = name
        self.place = place
        self.date = date
        self.description = description
        self.time_control = time_control
        self.selected_players_id = selected_players
        self.number_of_rounds = number_of_rounds

    def get_serialized_tournament(self):
        serialized_tournament = {
            "id": self.id,
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "description": self.description,
            "time_control": self.time_control,
            "selected_players": self.selected_players_id,
            "number_of_rounds": self.number_of_rounds
        }
        tournaments_table.insert(serialized_tournament)

    @staticmethod
    def get_tournaments_data():  # get tournaments data
        tournaments = tournaments_table.all()
        tournaments_data = []
        for i in range(len(tournaments_table)):
            list_tournament = []
            list_tournament.append(tournaments[i]["id"])
            list_tournament.append(tournaments[i]["name"])
            list_tournament.append(tournaments[i]["time_control"])
            list_tournament.append(tournaments[i]["number_of_rounds"])
            tournaments_data.append(list_tournament)
        return tournaments_data

    @staticmethod
    def get_tournaments_id():  # get tournaments data
        tournaments = tournaments_table.all()
        tournaments_id = []
        for i in range(len(tournaments_table)):
            tournaments_id.append(tournaments[i]["id"])
        return tournaments_id

    @staticmethod
    def get_data_from_tournament_id(tournament_id, index):
        selected_tournament = tournaments_table.search(User.id == tournament_id)
        data = selected_tournament[0][index]
        return data
