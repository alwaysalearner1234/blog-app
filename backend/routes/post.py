from flask import Blueprint, request, jsonify
from models import Post
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

post_bp = Blueprint('post', __name__)

@post_bp.route('/create', methods=['POST'])
@jwt_required()
def create_post():
    user_id = get_jwt_identity()
    data = request.json

    post = Post(title=data['title'], content=data['content'], user_id=user_id)
    db.session.add(post)
    db.session.commit()

    return jsonify({"msg": "Post created"})

@post_bp.route('/', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    return jsonify([{"id": p.id, "title": p.title, "content": p.content} for p in posts])
