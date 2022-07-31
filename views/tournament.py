from rich.console import Console
from rich import print

import re

console = Console()


class NewTournament:
    def name_entrie(self):  # tournament name
        name = console.input("[blue]Entrez le [bold green]Nom[/] du tournoi: ").capitalize()
        return name

    def place_entrie(self):  # tournament place
        place = console.input("[blue]Entrez le [bold green]Lieu[/] du tournoi: ")
        return place

    """tournament date regex"""

    def date_entrie(self):
        while True:
            regex = "\A[^0-9/]+\Z"
            date_entrie = console.input("[blue]Entrez la [bold green]DATE[/] du tournoi: ")
            try:
                if re.match(regex, date_entrie):
                    raise ValueError
                elif len(date_entrie) != 10:
                    raise FormatError
                elif date_entrie[2] != "/" or date_entrie[5] != "/":
                    raise FormatError
                elif date_entrie[0] == "/" or \
                        date_entrie[1] == "/" or \
                        date_entrie[3] == "/" or \
                        date_entrie[4] == "/" or \
                        date_entrie[6] == "/" or \
                        date_entrie[7] == "/" or \
                        date_entrie[8] == "/" or \
                        date_entrie[9] == "/":
                    raise FormatError
                else:
                    return date_entrie
            except ValueError:
                console.print('[bold red]Vous ne pouvez pas entrer des lettres ou des symboles (sauf "/")')

            except Exception as FormatError:
                console.print('[bold red]Vous devez rentrer la date du tournoi au format "DD/MM/YYYY')

    def description_entrie(self):  # tournament description
        description = console.input("[blue]Entrez la [bold green]DESCRIPTION[/] du tournoi: ")
        return description

    def time_control_entrie(self):  # tournament time_control
        while True:
            time_control = console.input("[blue]Sélectionner le chiffre du type de partie [bold green]bullet (1)[/], "
                                         "[bold green]blitz (2)[/] ou [bold green]coup rapide (3)[/]: ")
            if time_control == "1":
                type = "bullet"
                return type
            elif time_control == "2":
                type = "blitz"
                return type
            elif time_control == "3":
                type = "coup rapide"
                return type
            else:
                print("[bold red]vous devez choisir entre [bold green]'1'[/] [bold green]'2'[/] [bold green]'3'[/].")

    def selected_players_id_entrie(self, players_data):  # get all selected players id inside a list and verify error
        id_list = []
        selected_players_list = []
        for i in range(len(players_data)):  # get all players id inside a list
            id = int(players_data[i][0])
            id_list.append(id)
        while True:  # repeat input until you stop
            try:
                id = int(console.input(f"sélectionner l'id des participants (saisir '[bold blue]0[/]' quand tous les "
                                       f"joueurs sont séléctionnés): "))
                id_len = len(selected_players_list)
                if id == 0:
                    if id_len % 2 == 0:  # verify if selected players list is a pair number
                        return selected_players_list
                    raise LenError
                elif id not in id_list:  # error if id entrie is not inside players db
                    raise IndexError
                selected_players_list.append(id)
            except ValueError:
                console.print("[bold red]Vous devez saisir un id valide")
            except IndexError:
                console.print("[bold red]Vous devez saisir un id dans la liste")
            except Exception as LenError:
                console.print("[bold red]Vous devez saisir un nombre paire de joueurs avant de pouvoir valider")

    def number_of_rounds_entrie(self, maximum_rounds):  # verify maxmimum rounds numbers with maximum rounds
        while True:
            number_of_rounds = int(console.input(f"[blue]Entrez le nombre de [bold green]TOURS[/] du tournoi (maximum "
                                                 f"[bold blue]{maximum_rounds}[/]) : "))
            if number_of_rounds > maximum_rounds:
                console.print(f"[bold red]Vous ne pouvez pas séléctionner plus de {maximum_rounds} tours")
            else:
                return number_of_rounds
