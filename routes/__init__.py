def init_routes(app, session):
    from .search import pokemon, register_pokemon_routes
    register_pokemon_routes(session)
    app.register_blueprint(pokemon)