import os
from cassandra.cluster import Cluster
from PIL import Image
import io

class CassandraConfig:
    def __init__(self, nodes=['127.0.0.1']):
        self.cluster = Cluster(nodes)
        self.session = self.cluster.connect("pokemon_db")

    def close(self):
        if self.session:
            self.session.shutdown()
        if self.cluster:
            self.cluster.shutdown()

def create_table():
    self.session.execute("""
    CREATE TABLE IF NOT EXISTS pokemon_images (
        name TEXT PRIMARY KEY,
        image BLOB
    )
    """)
    print("Successfully created pokemon images table!")

def load_image(session, name, file_path):
    with open(file_path, 'rb') as f:
        image_data = f.read()

    session.execute("""
        INSERT INTO pokemon_images (name, image)
        VALUES (%s, %s)
    """, (name, image_data))

def main():
    cassandra_config = CassandraConfig()
    create_table()

    # Path to the main pokemon images 
    images_dir = "path/to/Pokemon Images DB/"

    for pokemon_folder in os.listdir(images_dir):
        pokemon_path = os.path.join(images_dir, pokemon_folder)
        
        if os.path.isdir(pokemon_path):
            for filename in os.listdir(pokemon_path):
                if filename.endswith(".png") and "_new" not in filename:
                    name = pokemon_folder  
                    file_path = os.path.join(pokemon_path, filename)
                    load_image(cassandra_config.session, name, file_path)
                    print(f"Loaded {name} from {file_path}")
                    break  

    cassandra_config.close()
    print("All images loaded successfully.")

if __name__ == "__main__":
    main()
