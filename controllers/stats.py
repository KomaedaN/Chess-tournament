from rich.console import Console
from views.stats import Stats
from models.tournament import Tournament
from models.player import Player
from models.match import Match
from models.turn import Turn

import os

console = Console()


class StatsController:
    def menu(self):
        choice = Stats().display_menu()
        if choice == 1:  # players menu stats
            os.system('cls' if os.name == 'nt' else 'clear')
            StatsController().players_menu()

        elif choice == 2:  # tournament menu stats
            os.system('cls' if os.name == 'nt' else 'clear')
            StatsController().tournament_menu()

        elif choice == 3:  # leave stats menu
            os.system('cls' if os.name == 'nt' else 'clear')

    """players stats"""

    def players_menu(self):    #
        data = Player.get_players_data()
        choice = Stats().display_players()
        if choice == 1:  # players by name
            os.system('cls' if os.name == 'nt' else 'clear')
            StatsController().players_sorted_by_name(data)

        elif choice == 2:  # players by rank
            os.system('cls' if os.name == 'nt' else 'clear')
            StatsController().players_sorted_by_rank(data)

        elif choice == 3:  # return to stats menu
            os.system('cls' if os.name == 'nt' else 'clear')
            StatsController().menu()

    def players_sorted_by_name(self, data):  # order and display players by name
        name_list = Stats().order_by_name(data)
        data_list = Player.get_data_from_name(name_list)
        Stats().display_players_by_name(data_list)

    def players_sorted_by_rank(self, data):  # order and display players by rank
        rank_list = Stats().order_by_rank(data)
        data_list = Player.get_data_from_rank(rank_list)
        Stats().display_players_by_rank(data_list)

    """tournaments stats"""

    def tournament_menu(self):
        data = Tournament.get_tournaments_data()  # get tournament data
        choice = Stats().display_tournaments()
        if choice == 1:  # players name from tournament
            os.system('cls' if os.name == 'nt' else 'clear')
            choice = Stats().display_all_tournaments_id(data)
            os.system('cls' if os.name == 'nt' else 'clear')
            StatsController().tournament_players(choice)

        elif choice == 2:  # turns from tournament
            os.system('cls' if os.name == 'nt' else 'clear')
            choice = Stats().display_all_tournaments_id(data)
            os.system('cls' if os.name == 'nt' else 'clear')
            StatsController().tournament_turns(choice)

        elif choice == 3:  # matchs from tournament
            os.system('cls' if os.name == 'nt' else 'clear')
            choice = Stats().display_all_tournaments_id(data)
            os.system('cls' if os.name == 'nt' else 'clear')
            StatsController().tournament_matchs(choice)

        elif choice == 4:  # return to stats menu
            os.system('cls' if os.name == 'nt' else 'clear')
            StatsController().menu()

    def tournament_players(self, choice):
        players_id = Tournament.get_data_from_tournament_id(choice, 'selected_players')
        data = Player.get_name_from_id_list(players_id)
        Stats().display_tournament_players(data)

    def tournament_turns(self, choice):
        turn_data = Turn.verify_tournament_id(choice)
        Stats().display_tournament_turns(turn_data)

    def tournament_matchs(self, choice):
        match_data = Match.verify_tournament_id(choice)
        Stats().display_tournament_matchs(match_data)
