from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User
import bcrypt
from bson.objectid import ObjectId

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    if User.find_by_email(data['email']):
        return jsonify({'error': 'User already exists'}), 409
    
    user_id = User.create(data)
    access_token = create_access_token(identity=str(user_id))
    
    return jsonify({
        'message': 'User created successfully',
        'access_token': access_token,
        'user_id': str(user_id)
    }), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('password'):
        return jsonify({'error': 'Missing email or password'}), 400
    
    user = User.find_by_email(data['email'])
    
    if not user or not bcrypt.checkpw(data['password'].encode(), user['password']):
        return jsonify({'error': 'Invalid email or password'}), 401
    
    access_token = create_access_token(identity=str(user['_id']))
    
    return jsonify({
        'message': 'Login successful',
        'access_token': access_token,
        'user_id': str(user['_id']),
        'name': user.get('name'),
        'role': user.get('role', 'user')
    }), 200

@bp.route('/profile', methods=['GET'])
@jwt_required()
def get_profile():
    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)
    
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({
        'user_id': str(user['_id']),
        'name': user.get('name'),
        'email': user.get('email'),
        'phone': user.get('phone'),
        'role': user.get('role'),
        'membership': user.get('membership')
    }), 200

@bp.route('/profile', methods=['PUT'])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    update_data = {}
    if 'name' in data:
        update_data['name'] = data['name']
    if 'phone' in data:
        update_data['phone'] = data['phone']
    
    User.collection.update_one(
        {'_id': ObjectId(user_id)},
        {'$set': update_data}
    )
    
    return jsonify({'message': 'Profile updated successfully'}), 200
