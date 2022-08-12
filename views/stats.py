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
        table.add_column("[italic #F8961E]Nom[/]", justify="left", style="#F94144")
        table.add_column("[italic #F8961E]Prenom[/]", justify="left", style="#277DA1")
        table.add_column("[italic #F8961E]Rank[/]", justify="left", style="#277DA1")
        table.add_column("[italic #F8961E]Elo[/]", justify="left", style="#277DA1")
        for i in range(len(data)):
            table.add_row(f"{data[i][0]}", f"{data[i][1]}", f"{data[i][2]}", f"{data[i][3]}")
        console.print(table, justify="center")
        console.input("Appuyez sur entrée pour revenir au menu principal")

    def order_by_rank(self, data):
        rank_list = []
        for i in range(len(data)):
            rank = data[i][3]
            rank_list.append(rank)
        return sorted(rank_list)

    def display_players_by_rank(self, data):
        table = Table()
        table.add_column("[italic #F8961E]Rank[/]", justify="left", style="#F94144")
        table.add_column("[italic #F8961E]Nom[/]", justify="left", style="#277DA1")
        table.add_column("[italic #F8961E]Prenom[/]", justify="left", style="#277DA1")
        table.add_column("[italic #F8961E]Elo[/]", justify="left", style="#277DA1")
        for i in range(len(data)):
            table.add_row(f"{data[i][0]}", f"{data[i][1]}", f"{data[i][2]}", f"{data[i][3]}")
        console.print(table, justify="center")
        console.input("Appuyez sur entrée pour revenir au menu principal")

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
        table.add_column("[italic #F8961E]Nom du tournoi[/]", justify="left", style="#277DA1")
        table.add_column("[italic #F8961E]Temps[/]", justify="center", style="#277DA1")
        for i in range(len(data)):
            table.add_row(f"{data[i][0]}", f"{data[i][1]}", f"{data[i][2]}")
        console.print(table, justify="center")
