from flask import Blueprint, request, jsonify
from crud.search import (
    get_pokemon_by_name,
    get_pokemon_by_type,
    get_pokemon_by_speed,
    get_pokemon_by_growth_and_catch_rate,
    get_pokemon_by_egg_group,
    get_pokemon_by_abilities
)
from cassandra.cluster import Session

pokemon = Blueprint('pokemon', __name__, url_prefix='/api/pokemon')

def register_pokemon_routes(session: Session):
    @pokemon.route('', methods=['GET'])
    def search_pokemon():
        """
        Search Pokémon by name or type.
        Example usage:
        - /api/pokemon?name=Pikachu
        - /api/pokemon?type=Fire
        """
        name = request.args.get('name')
        p_type = request.args.get('type')

        results = []
        if name:
            rows = get_pokemon_by_name(session, name)
        elif p_type:
            rows = get_pokemon_by_type(session, p_type)
        else:
            return jsonify({"error": "Please provide either 'name' or 'type' as a parameter"}), 400

        for row in rows:
            results.append(row._asdict())

        return jsonify(results)

    @pokemon.route('/speed', methods=['GET'])
    def get_fast_pokemon():
        """
        Retrieve Pokémon with speed_base >= min_speed.
        Example: /api/pokemon/speed?min_speed=100
        """
        min_speed = request.args.get('min_speed', type=int)
        if min_speed is None:
            return jsonify({"error": "Please provide 'min_speed' as a query parameter"}), 400

        rows = get_pokemon_by_speed(session, min_speed)
        results = [row._asdict() for row in rows]

        return jsonify(results)

    @pokemon.route('/growth_catch', methods=['GET'])
    def get_pokemon_by_growth_catch():
        """
        Retrieve Pokémon based on growth_rate and minimum catch_rate.
        Example: /api/pokemon/growth_catch?growth_rate=Medium Fast&min_catch_rate=50
        """
        growth_rate = request.args.get('growth_rate')
        min_catch_rate = request.args.get('min_catch_rate', type=int)

        if not growth_rate or min_catch_rate is None:
            return jsonify({"error": "Please provide both 'growth_rate' and 'min_catch_rate' as query parameters"}), 400

        results = get_pokemon_by_growth_and_catch_rate(session, growth_rate, min_catch_rate)
        return jsonify(results)


    @pokemon.route('/egg_group', methods=['GET'])
    def get_pokemon_by_egg_group_route():
        """
        Retrieve Pokémon by egg group.
        Example: /api/pokemon/egg_group?egg_group=Monster
        """
        egg_group = request.args.get('egg_group')
        if not egg_group:
            return jsonify({"error": "Please provide 'egg_group' as a query parameter"}), 400

        rows = get_pokemon_by_egg_group(session, egg_group)
        results = [row._asdict() for row in rows]

        return jsonify(results)

    @pokemon.route('/abilities', methods=['GET'])
    def get_pokemon_by_abilities_route():
        """
        Retrieve Pokémon by a specific ability.
        Example: /api/pokemon/abilities?ability=Intimidate
        """
        ability = request.args.get('ability')
        if not ability:
            return jsonify({"error": "Please provide 'ability' as a query parameter"}), 400

        rows = get_pokemon_by_abilities(session, ability)
        results = [row._asdict() for row in rows]

        return jsonify(results)