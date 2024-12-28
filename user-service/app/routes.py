from flask import Blueprint, request, jsonify
from app import db
from app.models import User

routes = Blueprint('routes', __name__)

@routes.route('/users', methods=['GET'])
def get_users():
    # Query all users
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "age": u.age} for u in users])

@routes.route('/users', methods=['POST'])
def create_user():
    # Create new user from request data
    data = request.get_json()
    new_user = User(name=data['name'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created!'}), 201
