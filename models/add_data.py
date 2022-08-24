from tinydb import TinyDB

db = TinyDB("db_player.json")
players_table = db.table("players")


class AddData:
    def add_players():  # verify players table and insert data if needed
        if len(players_table) > 0:
            return

        else:   # add 8 players for the table
            players_table.insert_multiple([
                {"id": 1, "name": "Alf", "first_name": "Louise", "birthday": "02/10/1995", "gender": "F",
                 "rank": 1, "score": 0.0, "elo": 0.0, "player_versus": []},

                {"id": 2, "name": "Meagan", "first_name": "Laurine", "birthday": "21/04/1989", "gender": "F",
                 "rank": 2, "score": 0.0, "elo": 0.0, "player_versus": []},

                {"id": 3, "name": "Bee", "first_name": "Maximilien", "birthday": "10/08/1997", "gender": "M",
                 "rank": 3, "score": 0.0, "elo": 0.0, "player_versus": []},

                {"id": 4, "name": "Scout", "first_name": "Rhys", "birthday": "25/12/2000", "gender": "M",
                 "rank": 4, "score": 0.0, "elo": 0.0, "player_versus": []},

                {"id": 5, "name": "Deacon", "first_name": "Maryann", "birthday": "02/11/1990", "gender": "F",
                 "rank": 5, "score": 0.0, "elo": 0.0, "player_versus": []},

                {"id": 6, "name": "Phebe", "first_name": "Richardine", "birthday": "06/04/1997", "gender": "F",
                 "rank": 6, "score": 0.0, "elo": 0.0, "player_versus": []},

                {"id": 7, "name": "Laryn", "first_name": "Ellen", "birthday": "14/10/1994", "gender": "F",
                 "rank": 7, "score": 0.0, "elo": 0.0, "player_versus": []},

                {"id": 8, "name": "Brenda", "first_name": "Leyton", "birthday": "11/11/2000", "gender": "M",
                 "rank": 8, "score": 0.0, "elo": 0.0, "player_versus": []}
            ])
