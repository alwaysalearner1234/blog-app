# 📝 Blog Platform with Comments

A full-stack **Blogging Platform** built using **Flask (Backend)** and **React (Frontend)** where users can create posts, comment, and interact with content.

---

## 🚀 Features

### 👤 User Features
- User Registration & Login (JWT Authentication)
- Create Blog Posts ✍️
- View All Posts 📄
- Comment on Posts 💬

### 🔐 Security
- JWT-based Authentication
- Protected Routes for Posts & Comments

---

## 🧠 Tech Stack

### Frontend
- React.js
- Axios

### Backend
- Flask
- Flask SQLAlchemy
- Flask JWT Extended
- Flask CORS

### Database
- SQLite (can upgrade to MySQL/PostgreSQL)

---

## 📁 Project Structure
blog-app/
│
├── backend/
│ ├── app.py
│ ├── models.py
│ ├── routes/
│ │ ├── auth.py
│ │ ├── post.py
│ │ ├── comment.py
│
├── frontend/
│ ├── src/
│ │ ├── App.js
│ │ ├── Home.js
│
└── README.md


---

## ⚙️ Installation & Setup

### 🔧 Backend Setup

```bash
cd backend
pip install flask flask_sqlalchemy flask_cors flask_jwt_extended
python app.py
🗄️ Initialize Database

Run once:

from app import app, db
with app.app_context():
    db.create_all()
🌐 Frontend Setup
cd frontend
npm install
npm start
🔐 API Endpoints
Auth
POST /auth/register → Register user
POST /auth/login → Login (returns JWT)
Posts
GET /posts/ → Get all posts
POST /posts/create → Create post (Protected)
Comments
POST /comments/add → Add comment (Protected)
GET /comments/<post_id> → Get comments for a post
🔑 Authentication

Uses JWT Tokens

Include token in headers:

Authorization: Bearer <your_token>
🌍 Future Enhancements
✏️ Edit & Delete Posts
❤️ Like/Upvote System
👤 User Profiles
🔍 Search & Filters
📱 Responsive UI
🌐 Deployment (Render + Vercel)
🎯 Learning Outcomes
Full-stack development
REST API design
Authentication & Authorization
Database relationships
Real-world project structure
🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

📜 License

This project is open-source and free to use.

👩‍💻 Author

Lidiya
GitHub: https://github.com/alwaysalearner1234


---

## ✅ After adding

```bash
git add README.md
git commit -m "Added README"
git push
