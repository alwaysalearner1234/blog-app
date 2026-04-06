from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User
from app import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(username=data['username'], password=data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created"})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username'], password=data['password']).first()

    if user:
        token = create_access_token(identity=user.id)
        return jsonify({"token": token})

    return jsonify({"msg": "Invalid credentials"}), 401
