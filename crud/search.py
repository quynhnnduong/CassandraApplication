# crud/search.py
from cassandra.cluster import Session
from cassandra.query import SimpleStatement
import re


def get_pokemon_by_name(session: Session, name: str):
    query = "SELECT * FROM pokemon WHERE pokemon = %s"
    return session.execute(query, (name,))

def get_pokemon_by_type(session: Session, p_type: str):
    query = "SELECT * FROM pokemon WHERE type = %s"
    return session.execute(query, (p_type,))

def get_pokemon_by_speed(session: Session, min_speed: int):
    query = "SELECT pokemon, speed_base, speed_min, speed_max FROM pokemon WHERE speed_base >= %s ALLOW FILTERING"
    return session.execute(query, (min_speed,))

def get_pokemon_by_growth_and_catch_rate(session: Session, growth_rate: str, min_catch_rate: int):
    query = "SELECT * FROM pokemon WHERE growth_rate = %s ALLOW FILTERING"
    rows = session.execute(query, (growth_rate,))
    
    results = []
    for row in rows:
        match = re.match(r"(\d+)", row.catch_rate)
        if match and int(match.group(1)) >= min_catch_rate:
            results.append(row._asdict())
    
    return results

def get_pokemon_by_egg_group(session: Session, egg_group: str):
    query = "SELECT * FROM pokemon WHERE egg_groups = %s ALLOW FILTERING"
    return session.execute(query, (egg_group,))

def get_pokemon_by_abilities(session: Session, ability: str):
    query = "SELECT * FROM pokemon WHERE abilities LIKE %s ALLOW FILTERING"
    return session.execute(query, (ability,))
