from flask import Flask, render_template, request
from config.config import CassandraConfig
from data.data_loader import DataLoader

app = Flask(__name__)

cassandra_config = CassandraConfig()
session = cassandra_config.connect()

# Initialize DataLoader and create table
# data_loader = DataLoader(session)
# data_loader.create_table()
# Uncomment the line below to load data from JSON once
# data_loader.load_from_json('data/dataset.json')

# Query functions
def get_pokemon_by_name(name):
    return session.execute("SELECT * FROM pokemon WHERE name = %s", (name,))

def get_pokemon_by_type(p_type):
    return session.execute("SELECT * FROM pokemon WHERE type CONTAINS %s", (p_type,))

# Flask Routes
@app.route('/')
def home():
    return render_template('search.html')

@app.route('/search', methods=['POST'])
def search():
    name = request.form.get('name')
    p_type = request.form.get('type')
    
    results = []
    if name:
        results = get_pokemon_by_name(name)
    elif p_type:
        results = get_pokemon_by_type(p_type)
    
    return render_template('results.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
