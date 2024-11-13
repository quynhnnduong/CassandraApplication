import csv

class DataLoader:
    def __init__(self, session):
        self.session = session

    def create_table(self):
        self.session.execute("""
        CREATE TABLE IF NOT EXISTS pokemon (
            name TEXT PRIMARY KEY,
            type TEXT,
            species TEXT,
            height FLOAT,
            weight FLOAT,
            abilities TEXT,
            base_hp INT,
            base_attack INT,
            base_defense INT,
            base_speed INT
        )
        """)

    def load_from_csv(self, file_path):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.session.execute("""
                INSERT INTO pokemon (name, type, species, height, weight, abilities, base_hp, base_attack, base_defense, base_speed)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, (row['Pokemon'], row['Type'], row['Species'], float(row['Height']),
                      float(row['Weight']), row['Abilities'], int(row['Base HP']),
                      int(row['Base Attack']), int(row['Base Defense']), int(row['Base Speed'])))
