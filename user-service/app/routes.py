from flask import Blueprint, request, jsonify
from app.models import User, db

routes = Blueprint('routes', __name__)

@routes.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "age": u.age} for u in users])

@routes.route('/users', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(name=data['name'], age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User added!", "id": new_user.id}), 201
