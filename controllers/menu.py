from views.menu import MainMenu
from controllers.player import PlayerController

import os


class MenuController:
    def start_menu(self):
        while True:
            choice = MainMenu().menu_input()  # get input choice
            if choice == 1:  # Choice create player
                os.system('cls' if os.name == 'nt' else 'clear')
                PlayerController().create_player()
