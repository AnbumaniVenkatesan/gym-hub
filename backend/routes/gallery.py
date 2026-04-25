from flask import Blueprint, request, jsonify
from models import Gallery, User
from bson.objectid import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('gallery', __name__, url_prefix='/api/gallery')

@bp.route('', methods=['GET'])
def get_gallery():
    images = Gallery.get_all()
    return jsonify({
        'images': [{
            'id': str(img['_id']),
            'title': img.get('title'),
            'url': img.get('url'),
            'description': img.get('description')
        } for img in images]
    }), 200

@bp.route('', methods=['POST'])
@jwt_required()
def upload_image():
    user_id = get_jwt_identity()
    user = User.find_by_id(user_id)
    
    if user.get('role') != 'admin':
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    image_id = Gallery.create(data)
    
    return jsonify({
        'message': 'Image uploaded',
        'image_id': str(image_id)
    }), 201
