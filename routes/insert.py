from flask import Blueprint, request, jsonify
from crud.insert import create_pokemon
from crud.insert import randomize_pokemon
from cassandra.cluster import Session

pokemon_insert = Blueprint('pokemon_insert', __name__, url_prefix='/api/pokemon')

def register_pokemon_insert_routes(session: Session):
    @pokemon_insert.route('/insert', methods=['POST'])
    def insert_pokemon():
        """
        Insert a Pokémon into the database.
        Example:
        POST /api/pokemon/insert
        Body:
        {
            "pokemon": "Pikachu",
            "type": "Electric",
            "species": "Mouse Pokémon",
            "height": "0.4 m",
            "weight": "6.0 kg",
            "abilities": "1. Static, Lightning Rod (hidden ability)",
            "ev_yield": "2 Speed",
            "catch_rate": "190",
            "base_friendship": "70",
            "base_exp": 112,
            "growth_rate": "Medium Fast",
            "egg_groups": "Field, Fairy",
            "gender": "50% male, 50% female",
            "egg_cycles": "10",
            "hp_base": 35,
            "hp_min": 200,
            "hp_max": 294,
            "attack_base": 55,
            "attack_min": 130,
            "attack_max": 262,
            "defense_base": 40,
            "defense_min": 90,
            "defense_max": 214,
            "special_attack_base": 50,
            "special_attack_min": 120,
            "special_attack_max": 251,
            "special_defense_base": 50,
            "special_defense_min": 120,
            "special_defense_max": 251,
            "speed_base": 90,
            "speed_min": 180,
            "speed_max": 324
        }
        """
        try:
            # Get JSON data from the request body
            pokemon_data = request.get_json()
            
            # Validate data
            required_fields = [
                "pokemon", "type", "species", "height", "weight", "abilities", "ev_yield",
                "catch_rate", "base_friendship", "base_exp", "growth_rate", "egg_groups", "gender",
                "egg_cycles", "hp_base", "hp_min", "hp_max", "attack_base", "attack_min", "attack_max",
                "defense_base", "defense_min", "defense_max", "special_attack_base", "special_attack_min",
                "special_attack_max", "special_defense_base", "special_defense_min", "special_defense_max",
                "speed_base", "speed_min", "speed_max"
            ]
            
            missing_fields = [field for field in required_fields if field not in pokemon_data]
            if missing_fields:
                return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

            # Insert Pokémon into the database
            result = create_pokemon(session, pokemon_data)
            return jsonify(result), 201

        except Exception as e:
            return jsonify({"error": str(e)}), 500
        
    @pokemon_insert.route('/rand_insert', methods=['GET'])
    def post_random_pokemon():
        """
        Insert a random pokemon
        Example:
        /api/pokemon/rand_insert
        """
        rows = randomize_pokemon(session)
        results = [row._asdict() for row in rows]

        return jsonify(results)
