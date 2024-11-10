# app.py
from flask import Flask
from uuid import UUID

app = Flask(__name__)

# Import CRUD functions
from crud import create_user, get_user, list_users, delete_user

# Routes
@app.route('/users', methods=['POST'])
def create_user_route():
    return create_user()

@app.route('/users/<uuid:user_id>', methods=['GET'])
def get_user_route(user_id: UUID):
    return get_user(user_id)

@app.route('/users', methods=['GET'])
def list_users_route():
    return list_users()

@app.route('/users/<uuid:user_id>', methods=['DELETE'])
def delete_user_route(user_id: UUID):
    return delete_user(user_id)

if __name__ == '__main__':
    app.run(debug=True)
