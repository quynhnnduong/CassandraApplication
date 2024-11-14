from flask import Flask, jsonify
from config.config import CassandraConfig
from routes import init_routes
from cassandra.cluster import Session
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    cassandra_config = CassandraConfig()
    session = cassandra_config.connect()

    init_routes(app, session)

    @app.route('/health', methods=['GET'])
    def health_check():
        return jsonify({"status": "OK"}), 200

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
