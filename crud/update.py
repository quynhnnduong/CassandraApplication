from cassandra.cluster import Session

def update_pokemon(session: Session, pokemon_name: str, updated_data: dict):
    set_clause = ", ".join([f"{key} = ?" for key in updated_data.keys()])
    query = f"UPDATE pokemon SET {set_clause} WHERE pokemon = ?"

    parameters = list(updated_data.values())
    parameters.append(pokemon_name)
    
    session.execute(query, parameters)
    return {"message": f"Pokemon {pokemon_name} updated successfully."}
