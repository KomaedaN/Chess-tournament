from rich.console import Console
from rich import print

import re

console = Console()


class CreatePlayer:
    def name_entrie(self):
        """Name regex"""
        while True:
            regex = "\A[a-zA-Z-]+\Z"
            name = console.input("[blue]Entrez le [bold green]NOM[/] du joueur: ").capitalize()
            try:
                if re.match(regex, name):
                    return name
                else:
                    raise ValueError
            except ValueError:
                console.print('[bold red]Vous ne pouvez pas rentrer de nombres ou de symboles (uniquement un "-")')

    def first_name_entrie(self):
        """first_name regex"""
        while True:
            regex = "\A[a-zA-Z-]+\Z"
            first_name = console.input("[blue]Entrez le [bold green]PRENOM[/] du joueur: ").capitalize()
            try:
                if re.match(regex, first_name):
                    return first_name
                else:
                    raise ValueError
            except ValueError:
                console.print('[bold red]Vous ne pouvez pas rentrer de nombres ou de symboles (uniquement un "-")')

    def birthday_entrie(self):
        """birthday regex"""
        while True:
            regex = "\A[^0-9/]+\Z"
            birthday_entrie = console.input("[blue]Entrez la [bold green]DATE[/] de naissance du joueur: ")
            try:
                if re.match(regex, birthday_entrie):
                    raise ValueError
                elif len(birthday_entrie) != 10:
                    raise FormatError
                elif birthday_entrie[2] != "/" or birthday_entrie[5] != "/":
                    raise FormatError
                elif birthday_entrie[0] == "/" or \
                        birthday_entrie[1] == "/" or \
                        birthday_entrie[3] == "/" or \
                        birthday_entrie[4] == "/" or \
                        birthday_entrie[6] == "/" or \
                        birthday_entrie[7] == "/" or \
                        birthday_entrie[8] == "/" or \
                        birthday_entrie[9] == "/":
                    raise FormatError
                else:
                    return birthday_entrie
            except ValueError:
                console.print('[bold red]Vous ne pouvez pas entrer des lettres ou des symboles (sauf "/")')

            except Exception as FormatError:
                console.print('[bold red]Vous devez rentrer la date de naissance au format "DD/MM/YYYY')

    def gender_entrie(self):
        """gender regex"""
        while True:
            regex = "[^MFmf]"
            gender = console.input("[blue]Entrez le [bold green]GENRE[/] du joueur: ").capitalize()
            try:
                if re.match(regex, gender):
                    raise FormatError
                elif len(gender) != 1:
                    raise FormatError
                else:
                    return gender
            except Exception as FormatError:
                print('[bold red]Vous devez sélectionner entre [#d90429]M[/] et [#d90429]F[/] uniquement')