from flask import Blueprint, request, jsonify
from crud.delete import delete_pokemon
from cassandra.cluster import Session

pokemon_delete = Blueprint('pokemon_delete', __name__, url_prefix='/api/pokemon')

def register_pokemon_delete_routes(session: Session):
    @pokemon_delete.route('/delete', methods=['DELETE'])
    def delete_pokemon_route():
        """
        Delete a Pokémon from the database by its name.
        Example:
        DELETE /api/pokemon/delete?name=Pikachu
        """
        try:
            # Get the Pokémon name from the query parameters
            pokemon_name = request.args.get('name')
            if not pokemon_name:
                return jsonify({"error": "Please provide 'name' as a query parameter"}), 400

            # Call the CRUD delete function
            result = delete_pokemon(session, pokemon_name)
            return jsonify(result), 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500
