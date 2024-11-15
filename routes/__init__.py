def init_routes(app, session):
    from .search import pokemon, register_pokemon_routes
    from .insert import pokemon_insert, register_pokemon_insert_routes
    from .update import pokemon_update, register_pokemon_update_routes
    from .delete import pokemon_delete, register_pokemon_delete_routes
    register_pokemon_routes(session)
    register_pokemon_insert_routes(session)
    register_pokemon_update_routes(session)
    register_pokemon_delete_routes(session)
    app.register_blueprint(pokemon)
    app.register_blueprint(pokemon_insert)
    app.register_blueprint(pokemon_update)
    app.register_blueprint(pokemon_delete)