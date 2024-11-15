from flask import Blueprint, request, jsonify
from crud.update import update_pokemon
from cassandra.cluster import Session

pokemon_update = Blueprint('pokemon_update', __name__, url_prefix='/api/pokemon')

def register_pokemon_update_routes(session: Session):
    @pokemon_update.route('/update', methods=['PUT'])
    def update_pokemon_route():
        """
        Update Pokémon details in the database.
        Example:
        PUT /api/pokemon/update
        Body:
        {
            "name": "Pikachu",
            "updated_data": {
                "type": "Electric, Fairy",
                "attack_base": 60,
                "speed_base": 95
            }
        }
        """
        try:
            # Get JSON data from the request
            data = request.get_json()
            if not data:
                return jsonify({"error": "Request body is missing"}), 400

            pokemon_name = data.get("name")
            updated_data = data.get("updated_data")

            if not pokemon_name or not updated_data:
                return jsonify({
                    "error": "Both 'name' and 'updated_data' must be provided in the request body"
                }), 400

            # Call the CRUD update function
            result = update_pokemon(session, pokemon_name, updated_data)
            return jsonify(result), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
