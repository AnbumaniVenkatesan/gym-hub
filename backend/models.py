from pymongo import MongoClient
from datetime import datetime
import bcrypt
from config import Config

client = MongoClient(Config.MONGODB_URI)
db = client['gymhub']

class User:
    collection = db['users']
    
    @staticmethod
    def create(data):
        hashed_password = bcrypt.hashpw(data['password'].encode(), bcrypt.gensalt())
        user = {
            'name': data.get('name'),
            'email': data.get('email'),
            'password': hashed_password,
            'phone': data.get('phone', ''),
            'role': data.get('role', 'user'),
            'membership': data.get('membership', None),
            'created_at': datetime.utcnow(),
            'updated_at': datetime.utcnow()
        }
        result = User.collection.insert_one(user)
        return result.inserted_id
    
    @staticmethod
    def find_by_email(email):
        return User.collection.find_one({'email': email})
    
    @staticmethod
    def find_by_id(user_id):
        from bson.objectid import ObjectId
        return User.collection.find_one({'_id': ObjectId(user_id)})

class Membership:
    collection = db['memberships']
    
    @staticmethod
    def create(data):
        membership = {
            'name': data.get('name'),
            'price': data.get('price'),
            'duration': data.get('duration'),  # months
            'features': data.get('features', []),
            'created_at': datetime.utcnow()
        }
        result = Membership.collection.insert_one(membership)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        return list(Membership.collection.find())

class Class:
    collection = db['classes']
    
    @staticmethod
    def create(data):
        gym_class = {
            'name': data.get('name'),
            'description': data.get('description'),
            'trainer_id': data.get('trainer_id'),
            'schedule': data.get('schedule'),
            'capacity': data.get('capacity'),
            'duration': data.get('duration'),
            'level': data.get('level'),
            'created_at': datetime.utcnow()
        }
        result = Class.collection.insert_one(gym_class)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        return list(Class.collection.find())

class Booking:
    collection = db['bookings']
    
    @staticmethod
    def create(data):
        booking = {
            'user_id': data.get('user_id'),
            'class_id': data.get('class_id'),
            'booking_date': datetime.utcnow(),
            'status': 'confirmed'
        }
        result = Booking.collection.insert_one(booking)
        return result.inserted_id
    
    @staticmethod
    def get_user_bookings(user_id):
        return list(Booking.collection.find({'user_id': user_id}))

class Trainer:
    collection = db['trainers']
    
    @staticmethod
    def create(data):
        trainer = {
            'name': data.get('name'),
            'specialty': data.get('specialty'),
            'experience': data.get('experience'),
            'bio': data.get('bio'),
            'image_url': data.get('image_url'),
            'created_at': datetime.utcnow()
        }
        result = Trainer.collection.insert_one(trainer)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        return list(Trainer.collection.find())

class Gallery:
    collection = db['gallery']
    
    @staticmethod
    def create(data):
        image = {
            'title': data.get('title'),
            'url': data.get('url'),
            'description': data.get('description'),
            'uploaded_at': datetime.utcnow()
        }
        result = Gallery.collection.insert_one(image)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        return list(Gallery.collection.find())

class Testimonial:
    collection = db['testimonials']
    
    @staticmethod
    def create(data):
        testimonial = {
            'user_id': data.get('user_id'),
            'name': data.get('name'),
            'rating': data.get('rating'),
            'message': data.get('message'),
            'created_at': datetime.utcnow()
        }
        result = Testimonial.collection.insert_one(testimonial)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        return list(Testimonial.collection.find())

class Contact:
    collection = db['contact_messages']
    
    @staticmethod
    def create(data):
        message = {
            'name': data.get('name'),
            'email': data.get('email'),
            'phone': data.get('phone'),
            'subject': data.get('subject'),
            'message': data.get('message'),
            'created_at': datetime.utcnow(),
            'status': 'new'
        }
        result = Contact.collection.insert_one(message)
        return result.inserted_id
    
    @staticmethod
    def get_all():
        return list(Contact.collection.find())
