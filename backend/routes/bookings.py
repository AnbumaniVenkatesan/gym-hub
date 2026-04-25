from flask import Blueprint, request, jsonify
from models import Booking
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('bookings', __name__, url_prefix='/api/bookings')

@bp.route('', methods=['POST'])
@jwt_required()
def create_booking():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    data['user_id'] = user_id
    booking_id = Booking.create(data)
    
    return jsonify({
        'message': 'Booking confirmed',
        'booking_id': str(booking_id)
    }), 201

@bp.route('', methods=['GET'])
@jwt_required()
def get_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.get_user_bookings(user_id)
    
    return jsonify({
        'bookings': [{
            'id': str(b['_id']),
            'class_id': b.get('class_id'),
            'booking_date': str(b.get('booking_date')),
            'status': b.get('status')
        } for b in bookings]
    }), 200

@bp.route('/<booking_id>', methods=['DELETE'])
@jwt_required()
def cancel_booking(booking_id):
    user_id = get_jwt_identity()
    
    booking = Booking.collection.find_one({'_id': ObjectId(booking_id)})
    
    if not booking or booking.get('user_id') != user_id:
        return jsonify({'error': 'Not found'}), 404
    
    Booking.collection.delete_one({'_id': ObjectId(booking_id)})
    
    return jsonify({'message': 'Booking cancelled'}), 200
