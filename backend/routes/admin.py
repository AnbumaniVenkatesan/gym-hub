from flask import Blueprint, request, jsonify
from models import User, Booking, Contact
from flask_jwt_extended import jwt_required, get_jwt_identity
from bson.objectid import ObjectId

bp = Blueprint('admin', __name__, url_prefix='/api/admin')

def admin_required(f):
    @jwt_required()
    def decorated_function(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.find_by_id(user_id)
        
        if user.get('role') != 'admin':
            return jsonify({'error': 'Unauthorized'}), 403
        
        return f(*args, **kwargs)
    
    decorated_function.__name__ = f.__name__
    return decorated_function

@bp.route('/dashboard', methods=['GET'])
@admin_required
def get_dashboard():
    total_users = User.collection.count_documents({})
    total_bookings = Booking.collection.count_documents({})
    total_messages = Contact.collection.count_documents({})
    
    return jsonify({
        'total_users': total_users,
        'total_bookings': total_bookings,
        'total_messages': total_messages
    }), 200

@bp.route('/users', methods=['GET'])
@admin_required
def get_users():
    users = list(User.collection.find({}))
    return jsonify({
        'users': [{
            'id': str(u['_id']),
            'name': u.get('name'),
            'email': u.get('email'),
            'role': u.get('role'),
            'phone': u.get('phone')
        } for u in users]
    }), 200

@bp.route('/messages', methods=['GET'])
@admin_required
def get_messages():
    messages = Contact.get_all()
    return jsonify({
        'messages': [{
            'id': str(m['_id']),
            'name': m.get('name'),
            'email': m.get('email'),
            'subject': m.get('subject'),
            'message': m.get('message'),
            'status': m.get('status')
        } for m in messages]
    }), 200

@bp.route('/messages/<message_id>/status', methods=['PUT'])
@admin_required
def update_message_status(message_id):
    data = request.get_json()
    
    Contact.collection.update_one(
        {'_id': ObjectId(message_id)},
        {'$set': {'status': data.get('status')}}
    )
    
    return jsonify({'message': 'Status updated'}), 200
