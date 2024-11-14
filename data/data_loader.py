import csv

class DataLoader:
    def __init__(self, session):
        self.session = session

    def create_table(self):
        self.session.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            pokemon text PRIMARY KEY,
            type text,
            species text,
            height list<text>,
            weight list<text>,
            abilities list<text>,
            ev_yield text,
            catch_rate text,
            base_friendship list<text>,
            base_exp int,
            growth_rate text,
            egg_groups text,
            gender text,
            egg_cycles text,
            hp_base int,
            hp_min int,
            hp_max int,
            attack_base int,
            attack_min int,
            attack_max int,
            defense_base int,
            defense_min int,
            defense_max int,
            special_attack_base int,
            special_attack_min int,
            special_attack_max int,
            special_defense_base int,
            special_defense_min int,
            special_defense_max int,
            speed_base int,
            speed_min int,
            speed_max int)
        """)
