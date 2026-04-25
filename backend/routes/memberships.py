from flask import Blueprint, request, jsonify
from models import Membership, User
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('memberships', __name__, url_prefix='/api/memberships')

@bp.route('', methods=['GET'])
def get_memberships():
    memberships = Membership.get_all()
    return jsonify({
        'memberships': [{
            'id': str(m['_id']),
            'name': m.get('name'),
            'price': m.get('price'),
            'duration': m.get('duration'),
            'features': m.get('features', [])
        } for m in memberships]
    }), 200

@bp.route('', methods=['POST'])
@jwt_required()
def create_membership():
    data = request.get_json()
    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)
    
    if user.get('role') != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    membership_id = Membership.create(data)
    
    return jsonify({
        'message': 'Membership created',
        'membership_id': str(membership_id)
    }), 201

@bp.route('/subscribe/<membership_id>', methods=['POST'])
@jwt_required()
def subscribe_membership(membership_id):
    user_id = get_jwt_identity()
    
    User.collection.update_one(
        {'_id': ObjectId(user_id)},
        {'$set': {'membership': membership_id}}
    )
    
    return jsonify({'message': 'Subscription successful'}), 200
