from tinydb import TinyDB

db = TinyDB("db_tournament.json")
tournaments_table = db.table("tournaments")
tournaments = tournaments_table.all()


class Tournament:
    def __init__(self, name, place, date, description="", time_control="", selected_players=[], number_of_rounds=4):
        self.id = (len(TinyDB("db_tournament.json").table("tournaments")) + 1)
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
