from cassandra.cluster import Session

def delete_pokemon(session: Session, pokemon_name: str):
    query = "DELETE FROM pokemon WHERE pokemon = ?"
    session.execute(query, (pokemon_name,))
    return {"message": f"Pokemon {pokemon_name} deleted successfully."}
