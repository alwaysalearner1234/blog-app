from flask import Blueprint, request, jsonify
from models import Comment
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

comment_bp = Blueprint('comment', __name__)

@comment_bp.route('/add', methods=['POST'])
@jwt_required()
def add_comment():
    user_id = get_jwt_identity()
    data = request.json

    comment = Comment(content=data['content'], user_id=user_id, post_id=data['post_id'])
    db.session.add(comment)
    db.session.commit()

    return jsonify({"msg": "Comment added"})

@comment_bp.route('/<int:post_id>', methods=['GET'])
def get_comments(post_id):
    comments = Comment.query.filter_by(post_id=post_id).all()
    return jsonify([{"content": c.content} for c in comments])
