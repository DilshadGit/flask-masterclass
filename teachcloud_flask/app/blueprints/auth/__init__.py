from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from ...models.user import User
from ...extensions import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    if not data.get('username') or not data.get('email') or not data.get('password'):
        return {"error": "Missing required fields"}, 400
    if User.query.filter_by(username=data['username']).first():
        return {"error": "Username already exists"}, 409
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return {"message": "User registered successfully", "user_id": user.id}, 201
