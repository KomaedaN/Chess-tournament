from models.player import Player
from views.player import CreatePlayer


class PlayerController:
    def create_player(self):
        """get all entries"""
        name = CreatePlayer().name_entrie()
        first_name = CreatePlayer().first_name_entrie()
        birthday = CreatePlayer().birthday_entrie()
        gender = CreatePlayer().gender_entrie()

        """Serialized entries"""
        player_entrie = Player(name, first_name, birthday, gender)
        player_entrie.get_serialized_player()
