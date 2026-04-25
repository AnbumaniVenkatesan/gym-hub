from flask import Flask, jsonify
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from config import Config, config
import os

app = Flask(__name__)
app.config.from_object(config[os.getenv('FLASK_ENV', 'development')])

# Initialize extensions
jwt = JWTManager(app)
CORS(app, origins=app.config['CORS_ORIGINS'])

# Import routes
from routes import auth, memberships, classes, trainers, bookings, gallery, testimonials, contact, admin

# Register blueprints
app.register_blueprint(auth.bp)
app.register_blueprint(memberships.bp)
app.register_blueprint(classes.bp)
app.register_blueprint(trainers.bp)
app.register_blueprint(bookings.bp)
app.register_blueprint(gallery.bp)
app.register_blueprint(testimonials.bp)
app.register_blueprint(contact.bp)
app.register_blueprint(admin.bp)

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({'error': 'Server error'}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
