from flask import Blueprint, request, jsonify
from models import Trainer
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('trainers', __name__, url_prefix='/api/trainers')

@bp.route('', methods=['GET'])
def get_trainers():
    trainers = Trainer.get_all()
    return jsonify({
        'trainers': [{
            'id': str(t['_id']),
            'name': t.get('name'),
            'specialty': t.get('specialty'),
            'experience': t.get('experience'),
            'bio': t.get('bio'),
            'image_url': t.get('image_url')
        } for t in trainers]
    }), 200

@bp.route('/<trainer_id>', methods=['GET'])
def get_trainer(trainer_id):
    trainer = Trainer.collection.find_one({'_id': ObjectId(trainer_id)})
    
    if not trainer:
        return jsonify({'error': 'Trainer not found'}), 404
    
    return jsonify({
        'id': str(trainer['_id']),
        'name': trainer.get('name'),
        'specialty': trainer.get('specialty'),
        'experience': trainer.get('experience'),
        'bio': trainer.get('bio'),
        'image_url': trainer.get('image_url')
    }), 200

@bp.route('', methods=['POST'])
@jwt_required()
def create_trainer():
    data = request.get_json()
    trainer_id = Trainer.create(data)
    
    return jsonify({
        'message': 'Trainer added',
        'trainer_id': str(trainer_id)
    }), 201
