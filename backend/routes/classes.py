from flask import Blueprint, request, jsonify
from models import Class, User
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('classes', __name__, url_prefix='/api/classes')

@bp.route('', methods=['GET'])
def get_classes():
    classes = Class.get_all()
    return jsonify({
        'classes': [{
            'id': str(c['_id']),
            'name': c.get('name'),
            'description': c.get('description'),
            'trainer_id': c.get('trainer_id'),
            'schedule': c.get('schedule'),
            'capacity': c.get('capacity'),
            'duration': c.get('duration'),
            'level': c.get('level')
        } for c in classes]
    }), 200

@bp.route('/<class_id>', methods=['GET'])
def get_class(class_id):
    gym_class = Class.collection.find_one({'_id': ObjectId(class_id)})
    
    if not gym_class:
        return jsonify({'error': 'Class not found'}), 404
    
    return jsonify({
        'id': str(gym_class['_id']),
        'name': gym_class.get('name'),
        'description': gym_class.get('description'),
        'trainer_id': gym_class.get('trainer_id'),
        'schedule': gym_class.get('schedule'),
        'capacity': gym_class.get('capacity'),
        'duration': gym_class.get('duration'),
        'level': gym_class.get('level')
    }), 200

@bp.route('', methods=['POST'])
@jwt_required()
def create_class():
    data = request.get_json()
    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)
    
    if user.get('role') != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    class_id = Class.create(data)
    
    return jsonify({
        'message': 'Class created',
        'class_id': str(class_id)
    }), 201
