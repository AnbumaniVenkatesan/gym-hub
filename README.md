# 💪 GymHub - Complete Gym Management Website

A full-featured gym management website built with Python Flask backend and HTML/CSS/JavaScript frontend.

## 🏋️ Features

✅ **Membership Plans** - Different tiers with pricing and benefits
✅ **Class Scheduling** - Browse and book fitness classes
✅ **Trainer Profiles** - Expert trainers with specialties
✅ **Member Portal** - Secure login and profile management
✅ **Class Booking System** - Reserve spots in classes
✅ **Gallery** - Showcase facilities and transformations
✅ **Testimonials** - Member reviews and ratings
✅ **Contact Form** - Get in touch functionality
✅ **Admin Dashboard** - Manage users, revenue, and reports

## 🛠️ Tech Stack

- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Backend**: Python Flask
- **Database**: MongoDB
- **Authentication**: JWT (JSON Web Tokens)

## 📁 Project Structure

```
gym-hub/
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── models.py
│   ├── requirements.txt
│   ├── routes/
│   │   ├── auth.py
│   │   ├── memberships.py
│   │   ├── classes.py
│   │   ├── trainers.py
│   │   ├── bookings.py
│   │   ├── gallery.py
│   │   ├── testimonials.py
│   │   ├── contact.py
│   │   └── admin.py
│   └── .env
├── frontend/
│   ├── index.html
│   ├── css/
│   │   ├── style.css
│   │   ├── responsive.css
│   │   └── animations.css
│   ├── js/
│   │   └── main.js
│   └── pages/
│       ├── login.html
│       ├── memberships.html
│       ├── classes.html
│       ├── trainers.html
│       ├── gallery.html
│       ├── contact.html
│       └── admin.html
└── .gitignore
```

## 🚀 Getting Started

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
```

Backend runs on: `http://localhost:5000`

### Frontend Setup

```bash
cd frontend
python -m http.server 8000
```

Frontend runs on: `http://localhost:8000`

### Database Setup

Make sure MongoDB is installed and running:

```bash
mongod
```

## 📚 API Endpoints

### Authentication
- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - User login
- `POST /api/auth/profile` - Get user profile
- `PUT /api/auth/profile` - Update profile

### Memberships
- `GET /api/memberships` - Get all plans
- `POST /api/memberships/subscribe/<id>` - Subscribe to plan

### Classes
- `GET /api/classes` - Get all classes
- `GET /api/classes/<id>` - Get class details
- `POST /api/classes` - Create class (Admin)

### Bookings
- `POST /api/bookings` - Create booking
- `GET /api/bookings` - Get user bookings
- `DELETE /api/bookings/<id>` - Cancel booking

### Trainers
- `GET /api/trainers` - Get all trainers
- `GET /api/trainers/<id>` - Get trainer details

### Gallery
- `GET /api/gallery` - Get gallery images
- `POST /api/gallery` - Upload image (Admin)

### Testimonials
- `GET /api/testimonials` - Get all testimonials
- `POST /api/testimonials` - Create testimonial

### Contact
- `POST /api/contact` - Send contact message

### Admin
- `GET /api/admin/dashboard` - Dashboard stats
- `GET /api/admin/users` - Manage users
- `GET /api/admin/messages` - Get messages
- `PUT /api/admin/messages/<id>/status` - Update message status

## 🔐 Authentication

The application uses JWT tokens for authentication. Upon login, a token is provided and must be included in the Authorization header:

```
Authorization: Bearer <token>
```

## 👨‍💼 Default Admin Credentials

- Email: `admin@gymhub.com`
- Password: `admin123`

## 🎨 Frontend Pages

1. **Home** - Landing page with features overview
2. **Memberships** - Available membership plans
3. **Classes** - Browse and book classes
4. **Trainers** - Meet the team
5. **Gallery** - Facility showcase
6. **Contact** - Get in touch
7. **Login** - User authentication
8. **Admin** - Management dashboard

## 💾 Database Models

- **User** - Members and admins
- **Membership** - Subscription plans
- **Class** - Fitness classes
- **Booking** - Class reservations
- **Trainer** - Trainer profiles
- **Gallery** - Images
- **Testimonial** - Reviews
- **Contact** - Messages

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests.

## 📄 License

MIT License - feel free to use this project for your gym!

## 💬 Support

For issues or questions, please create an issue in the repository.

---

**Built with ❤️ for fitness enthusiasts**
