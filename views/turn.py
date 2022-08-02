from rich.console import Console
from rich import print
from rich.table import Table

import re

console = Console()
table = Table()


class Turns:
    def display_turns(self, first_half_players, second_half_players, current_turn, match_number):
        table.add_column(f"[#F3722C]Tour {current_turn}[/]", justify="center", style="#277DA1")
        for i in range(match_number):
            match_counter = i + 1
            table.add_row("")
            table.add_row(
                f"[italic underline #277DA1]Match {match_counter}[/]: [bold #F94144]{first_half_players[i]}[/] "
                f"vs "
                f"[bold #F94144]{second_half_players[i]}[/]")
            table.add_row("")
        console.print(table, justify="center")
