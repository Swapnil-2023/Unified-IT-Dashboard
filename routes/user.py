from flask import Blueprint, request, jsonify
from models.user import User
from models import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([
        {
            "id": u.id,
            "name": u.name,
            "role": u.role
        } for u in users
    ])

@user_bp.route('/users', methods=['POST'])
def add_user():
    data = request.json

    user = User(
        name=data['name'],
        email=data['email'],
        password=data['password'],
        role=data['role']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User added"})
@user_bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({"message": "User deleted"})