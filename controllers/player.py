from models.player import Player
from models.add_data import AddData
from views.player import CreatePlayer


class PlayerController:
    def create_player(self):
        AddData.add_players()
        name_data = Player.get_all_name()
        """get all entries"""
        name = CreatePlayer().name_entrie(name_data)
        first_name = CreatePlayer().first_name_entrie()
        birthday = CreatePlayer().birthday_entrie()
        gender = CreatePlayer().gender_entrie()

        """Serialized entries"""
        player_entries = Player(name, first_name, birthday, gender)
        player_entries.get_serialized_player()
