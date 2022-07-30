from tinydb import TinyDB

db = TinyDB("db_tournament.json")
tournaments_table = db.table("tournaments")
tournaments = tournaments_table.all()


class Tournament:

    def __init__(self, name, place, date, description="", number_of_rounds=4, selected_players=[], time_control=""):
        self.id = (len(TinyDB("db_tournament.json").table("tournaments")) + 1)
        self.name = name
        self.place = place
        self.date = date
        self.description = description
        self.number_of_rounds = number_of_rounds
        self.selected_players_id = selected_players
        self.time_control = time_control

    def get_serialized_tournament(self):
        serialized_tournament = {
            "id": self.id,
            "name": self.name,
            "place": self.place,
            "date": self.date,
            "description": self.description,
            "number_of_rounds": self.number_of_rounds,
            "selected_players": self.selected_players_id,
            "time_control": self.time_control
        }
        tournaments_table.insert(serialized_tournament)
