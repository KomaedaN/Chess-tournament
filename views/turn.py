from rich.console import Console
from rich import print
from rich.table import Table
from models.player import Player

import re

console = Console()


class Turns:
    def display_turns(self, players, current_turn, match_number):
        table = Table()
        table.add_column(f"[#F3722C]Tour {current_turn}[/]", justify="center", style="#277DA1")
        for i in range(match_number):
            match_counter = i + 1
            table.add_row("")
            table.add_row(
                f"[italic underline #277DA1]Match {match_counter}[/]: [bold #F94144]{players[i][0]}[/] "
                f"vs "
                f"[bold #F94144]{players[i][1]}[/]")
            table.add_row("")
        console.print(table, justify="center")
        for i in range(match_number):
            current_match = i + 1
            Turns().score_result(current_match, players, i)

    def score_result(self, current_match, players, i):
        regex = "[^VDNvdn]"
        while True:
            player = players[i]
            first_result_entrie = console.input(
                f"Match {current_match}: Entrez le résultat de {player[0]} (Vous devez saisir V, D ou N): ").capitalize()
            try:
                if re.match(regex, first_result_entrie):
                    raise FormatError
                elif len(first_result_entrie) != 1:
                    raise FormatError
                else:
                    score_number = Turns().convert_to_point(first_result_entrie)
                    Player.update_player_score(player[0], score_number)
                    break
            except Exception as FormatError:
                print('[bold red]Vous devez saisir [#d90429]V[/], [#d90429]D[/] ou [#d90429]N[/] uniquement')

        while True:
            second_result_entrie = console.input(
                f"Match {current_match}: Entrez le résultat de {player[1]} (Vous devez saisir V, D ou N): ").capitalize()
            try:
                if re.match(regex, second_result_entrie):
                    raise ValueError
                elif len(second_result_entrie) != 1:
                    raise ValueError
                elif first_result_entrie == "N" and second_result_entrie != "N":
                    raise FailEntrie
                elif second_result_entrie == "N" and first_result_entrie != "N":
                    raise FailEntrie
                elif first_result_entrie == second_result_entrie and first_result_entrie != "N" and second_result_entrie != "N":
                    raise FailEntrie
                else:
                    score_number = Turns().convert_to_point(second_result_entrie)
                    Player.update_player_score(player[1], score_number)
                    break
            except ValueError:
                console.print('[bold red]Vous devez saisir [#d90429]V[/], [#d90429]D[/] ou [#d90429]N[/] uniquement')

            except Exception as FailEntrie:
                console.print('[bold red]Vous devez saisir le résultat [#d90429]valide[/]')

    def convert_to_point(self, player_result):
        if player_result == "V":
            return 1
        elif player_result == "D":
            return 0
        elif player_result == "N":
            return 0.5
