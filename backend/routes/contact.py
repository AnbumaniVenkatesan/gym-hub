from flask import Blueprint, request, jsonify
from models import Contact

bp = Blueprint('contact', __name__, url_prefix='/api/contact')

@bp.route('', methods=['POST'])
def send_contact():
    data = request.get_json()
    
    if not data or not data.get('email') or not data.get('message'):
        return jsonify({'error': 'Missing required fields'}), 400
    
    contact_id = Contact.create(data)
    
    return jsonify({
        'message': 'Message sent successfully',
        'contact_id': str(contact_id)
    }), 201
