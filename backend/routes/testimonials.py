from flask import Blueprint, request, jsonify
from models import Testimonial
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('testimonials', __name__, url_prefix='/api/testimonials')

@bp.route('', methods=['GET'])
def get_testimonials():
    testimonials = Testimonial.get_all()
    return jsonify({
        'testimonials': [{
            'id': str(t['_id']),
            'name': t.get('name'),
            'rating': t.get('rating'),
            'message': t.get('message')
        } for t in testimonials]
    }), 200

@bp.route('', methods=['POST'])
@jwt_required()
def create_testimonial():
    user_id = get_jwt_identity()
    data = request.get_json()
    
    data['user_id'] = user_id
    testimonial_id = Testimonial.create(data)
    
    return jsonify({
        'message': 'Testimonial created',
        'testimonial_id': str(testimonial_id)
    }), 201
