from rich.console import Console
from rich import print
from rich.table import Table
from models.player import Player
from models.match import Match
import re

console = Console()


class Turns:
    def display_turns(self, players, current_turn, match_number, match_id):  # display all matchs from a turn
        table = Table()
        table.add_column(f"[#F3722C]Tour {current_turn}[/]", justify="center", style="#277DA1")
        for i in range(match_number):
            match_counter = i + 1
            table.add_row("")
            table.add_row(
                f"[italic underline #277DA1]Match {match_counter}[/]: [bold #90BE6D]{players[i][0]}[/] "
                f"[bold #F94144]vs[/] "
                f"[bold #90BE6D]{players[i][1]}[/]")
            table.add_row("")
        console.print(table, justify="center")
        for i in range(match_number):
            current_match = i + 1
            Turns().score_result(current_match, players, i, match_id)

    def score_result(self, current_match, players, i, match_id):  # result entrie regex
        regex = "[^VDNvdn]"
        while True:
            player = players[i]
            first_result_entrie = console.input(
                f"[bold #43AA8B]Match[/] [bold #F94144]{current_match}:[/] Entrez le résultat du joueur "
                f"'{player[0]}' (Vous devez saisir [bold #90BE6D]V[/], [bold #F94144]D[/] ou [bold #277DA1]N[/]): ")\
                .capitalize()
            try:
                if re.match(regex, first_result_entrie):
                    raise ValueError
                elif len(first_result_entrie) != 1:
                    raise ValueError
                else:
                    score_number = Turns().convert_to_point(first_result_entrie)
                    Player.update_player_score(player[0], score_number)
                    Match.update_players_score(player[0], score_number, match_id[i], 'player_1_result')
                    break
            except ValueError:
                print('[bold red]Vous devez saisir [#d90429]V[/], [#d90429]D[/] ou [#d90429]N[/] uniquement')

        while True:
            second_result_entrie = console.input(
                f"[bold #43AA8B]Match[/] [bold #F94144]{current_match}:[/] Entrez le résultat du joueur "
                f"'{player[1]}' (Vous devez saisir [bold #90BE6D]V[/], [bold #F94144]D[/] ou [bold #277DA1]N[/]): ")\
                .capitalize()
            try:
                if re.match(regex, second_result_entrie):
                    raise ValueError
                elif len(second_result_entrie) != 1:
                    raise ValueError
                elif first_result_entrie == "N" and second_result_entrie != "N":
                    raise NameError
                elif second_result_entrie == "N" and first_result_entrie != "N":
                    raise NameError
                elif first_result_entrie == second_result_entrie and first_result_entrie != "N" and \
                        second_result_entrie != "N":
                    raise NameError
                else:
                    score_number = Turns().convert_to_point(second_result_entrie)
                    Player.update_player_score(player[1], score_number)
                    Match.update_players_score(player[0], score_number, match_id[i], 'player_2_result')
                    break
            except ValueError:
                console.print('[bold red]Vous devez saisir [#d90429]V[/], [#d90429]D[/] ou [#d90429]N[/] uniquement')

            except NameError:
                console.print('[bold red]Vous devez saisir le résultat [#d90429]valide[/]')

    def convert_to_point(self, player_result):  # convert result entrie into point
        if player_result == "V":
            return 1
        elif player_result == "D":
            return 0
        elif player_result == "N":
            return 0.5
