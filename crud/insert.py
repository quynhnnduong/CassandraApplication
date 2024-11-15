import random
from cassandra.cluster import Session

def create_pokemon(session: Session, pokemon_data: dict):
    query = """
    INSERT INTO pokemon (
        pokemon, type, species, height, weight, abilities, ev_yield,
        catch_rate, base_friendship, base_exp, growth_rate, egg_groups, gender, egg_cycles,
        hp_base, hp_min, hp_max, attack_base, attack_min, attack_max,
        defense_base, defense_min, defense_max, special_attack_base, special_attack_min,
        special_attack_max, special_defense_base, special_defense_min, special_defense_max,
        speed_base, speed_min, speed_max
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """
    session.execute(query, (
        pokemon_data['pokemon'], pokemon_data['type'], pokemon_data['species'], pokemon_data['height'],
        pokemon_data['weight'], pokemon_data['abilities'], pokemon_data['ev_yield'],
        pokemon_data['catch_rate'], pokemon_data['base_friendship'], pokemon_data['base_exp'],
        pokemon_data['growth_rate'], pokemon_data['egg_groups'], pokemon_data['gender'],
        pokemon_data['egg_cycles'], pokemon_data['hp_base'], pokemon_data['hp_min'], pokemon_data['hp_max'],
        pokemon_data['attack_base'], pokemon_data['attack_min'], pokemon_data['attack_max'],
        pokemon_data['defense_base'], pokemon_data['defense_min'], pokemon_data['defense_max'],
        pokemon_data['special_attack_base'], pokemon_data['special_attack_min'], pokemon_data['special_attack_max'],
        pokemon_data['special_defense_base'], pokemon_data['special_defense_min'], pokemon_data['special_defense_max'],
        pokemon_data['speed_base'], pokemon_data['speed_min'], pokemon_data['speed_max']
    ))
    return {"message": f"Pokemon {pokemon_data['pokemon']} created successfully."}

def randomize_pokemon(session: Session):
    pokemon = session.execute("SELECT * FROM pokemon LIMIT 1 ALLOW FILTERING").one()
    if not pokemon:
        return None

    # Randomize stats
    random_factor = random.randint(1, 10)
    pokemon.attack_base = pokemon.attack_base + random_factor
    pokemon.hp_base = pokemon.hp_base + random_factor
    pokemon.pokemon += str(random.randint(1,1000000000))
    create_pokemon(session, pokemon)