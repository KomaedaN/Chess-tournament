from rich.console import Console
from rich.table import Table

console = Console()


class Stats:
    def display_menu(self):  # first stats menu
        menu_table = Table()
        menu_table.add_column("[#F8961E]Sélectionner une option[/]", justify="left", style="#90BE6D")
        menu_table.add_row("")
        menu_table.add_row("[#F94144]1 -[/] Afficher les joueurs")
        menu_table.add_row("")
        menu_table.add_row("[#F94144]2 -[/] Afficher les tournois")
        menu_table.add_row("")
        menu_table.add_row("[#F94144]3 -[/] Retour au menu principal")
        menu_table.add_row("")
        console.print(menu_table, justify="center")
        menu_choice = int(console.input("[#277DA1]Entrez votre choix: "))
        return menu_choice

    """Display players stats"""

    def display_players(self):
        menu_table = Table()
        menu_table.add_column("[#F8961E]Joueurs[/]", justify="left", style="#90BE6D")
        menu_table.add_row("")
        menu_table.add_row("[#F94144]1 -[/] Afficher les joueurs par ordre alphabétique")
        menu_table.add_row("")
        menu_table.add_row("[#F94144]2 -[/] Afficher les joueurs en fonction du rang")
        menu_table.add_row("")
        menu_table.add_row("[#F94144]3 -[/] Précédent")
        menu_table.add_row("")
        console.print(menu_table, justify="center")
        choice = int(console.input("[#277DA1]Entrez votre choix: "))
        return choice

    def order_by_name(self, data):
        name_list = []
        for i in range(len(data)):
            name = data[i][1]
            name_list.append(name)
        return sorted(name_list)

    def display_players_by_name(self, data):
        table = Table()
        table.add_column("[italic #F8961E]Nom[/]", justify="left", style="#90BE6D")
        table.add_column("[italic #F8961E]Prenom[/]", justify="left", style="#90BE6D")
        table.add_column("[italic #F8961E]Rank[/]", justify="center", style="#F3722C")
        table.add_column("[italic #F8961E]Elo[/]", justify="center", style="#F3722C")
        for i in range(len(data)):
            table.add_row(f"{data[i][0]}", f"{data[i][1]}", f"{data[i][2]}", f"{data[i][3]}")
        console.print(table, justify="center")
        console.input("[bold #43AA8B]Appuyez sur entrée pour revenir au menu principal")

    def order_by_rank(self, data):
        rank_list = []
        for i in range(len(data)):
            rank = data[i][3]
            rank_list.append(rank)
        return sorted(rank_list)

    def display_players_by_rank(self, data):
        table = Table()
        table.add_column("[italic #F8961E]Rank[/]", justify="center", style="#F3722C")
        table.add_column("[italic #F8961E]Nom[/]", justify="left", style="#90BE6D")
        table.add_column("[italic #F8961E]Prenom[/]", justify="left", style="#90BE6D")
        table.add_column("[italic #F8961E]Elo[/]", justify="center", style="#F3722C")
        for i in range(len(data)):
            table.add_row(f"{data[i][0]}", f"{data[i][1]}", f"{data[i][2]}", f"{data[i][3]}")
        console.print(table, justify="center")
        console.input("[bold #43AA8B]Appuyez sur entrée pour revenir au menu principal")

    """Display tournaments stats"""

    def display_tournaments(self):
        menu_table = Table()
        menu_table.add_column("[#F8961E]Tournoi[/]", justify="left", style="#90BE6D")
        menu_table.add_row("")
        menu_table.add_row("[#F94144]1 -[/] Afficher les joueurs d'un tournoi")
        menu_table.add_row("")
        menu_table.add_row("[#F94144]2 -[/] Afficher tous les tours d'un tournoi")
        menu_table.add_row("")
        menu_table.add_row("[#F94144]3 -[/] Afficher tous les matchs d'un tournoi")
        menu_table.add_row("")
        menu_table.add_row("[#F94144]4 -[/] Précédent")
        menu_table.add_row("")
        console.print(menu_table, justify="center")
        choice = int(console.input("[#277DA1]Entrez votre choix: "))
        return choice

    def display_all_tournaments_id(self, data):
        table = Table()
        table.add_column("[italic #F8961E]Id[/]", justify="left", style="#F94144")
        table.add_column("[italic #F8961E]Nom du tournoi[/]", justify="left", style="#F9844A")
        table.add_column("[italic #F8961E]Temps[/]", justify="center", style="#90BE6D")
        list_id = []
        for i in range(len(data)):
            list_id.append(data[i][0])
            table.add_row(f"{data[i][0]}", f"{data[i][1]}", f"{data[i][2]}")
        console.print(table, justify="center")
        while True:
            try:
                choice = int(console.input("[#43AA8B]Sélectionner l'id d'un tournoi pour avoir plus d'informations: "))
                if choice not in list_id:
                    raise ValueError
                else:
                    return choice
            except ValueError:
                console.print("[bold red]Le tournoi choisi n'existe pas")

    def display_tournament_players(self, data):
        table = Table()
        table.add_column("[italic #F8961E]Joueurs du tournoi[/]", justify="center", style="#F94144")
        for i in range(len(data)):
            table.add_row(f"{data[i]}")
        console.print(table, justify="center")
        console.input("[bold #43AA8B]Appuyez sur entrée pour revenir au menu principal")

    def display_tournament_turns(self, turns_data):
        table = Table()
        table.add_column(f"[italic #F94144]Tours[/]", justify="left")
        table.add_column(f"[italic #F94144]id des matchs[/]", justify="left")
        for i in range(len(turns_data)):
            """data for table"""
            current_turn = turns_data[i][0]
            match_id = turns_data[i][1]
            """display matchs data"""
            table.add_row(f"[bold #F8961E]Tour {current_turn}[/]",
                          f"[bold #43AA8B]Matchs:[/] [bold #F9844A]{match_id}[/]")
            table.add_row("")
        console.print(table, justify="center")
        console.input("[bold #43AA8B]Appuyez sur entrée pour revenir au menu principal")

    def display_tournament_matchs(self, match_data):
        table = Table()
        table.add_column(f"[italic #F94144]Matchs[/]", justify="left")
        table.add_column(f"[italic #F94144]Joueur 1[/]", justify="left")
        table.add_column(f"[italic #F94144]Joueur 2[/]", justify="left")
        for i in range(len(match_data)):
            """data for table"""
            current_match = match_data[i][0]
            player_1 = match_data[i][1]
            player_1_result = match_data[i][2]
            player_2 = match_data[i][3]
            player_2_result = match_data[i][4]
            """display matchs data"""
            table.add_row(f"[bold #F8961E]Match {current_match}[/]",
                          f"[bold #43AA8B]{player_1}:[/] [bold #F9844A]{player_1_result}[/]",
                          f"[bold #43AA8B]{player_2}:[/]  [bold #F9844A]{player_2_result}[/]")
            table.add_row("")
        console.print(table, justify="center")
        console.input("[bold #43AA8B]Appuyez sur entrée pour revenir au menu principal")
