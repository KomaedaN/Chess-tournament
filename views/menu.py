from rich.console import Console
from rich import print
from rich.table import Table

console = Console()


class MainMenu:
    """display main menu"""

    def menu_input(self):
        console.rule("[bold #F3722C]MENU PRINCIPAL", style="#F9C74F")
        table = Table()
        table.add_column("[#F8961E]TOURNOI D'ECHEC [/]", justify="left", style="#90BE6D")
        table.add_row("")
        table.add_row("[#F94144]1 -[/] Ajouter un nouveau joueur")
        table.add_row("")
        table.add_row("[#F94144]2 -[/] Créer un tournoi")
        table.add_row("")
        table.add_row("[#F94144]3 -[/] Lancer un tournoi")
        table.add_row("")
        table.add_row("[#F94144]4 -[/] Données")
        table.add_row("")
        table.add_row("[#F94144]5 -[/] Quitter le programme")
        table.add_row("")
        console.print(table, justify="center")
        menu_choice = int(console.input("[#277DA1]Entrez votre choix: "))

        return menu_choice
