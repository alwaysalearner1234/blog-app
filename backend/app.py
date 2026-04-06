from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secretkey'

db = SQLAlchemy(app)
CORS(app)
jwt = JWTManager(app)

from routes.auth import auth_bp
from routes.post import post_bp
from routes.comment import comment_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(post_bp, url_prefix='/posts')
app.register_blueprint(comment_bp, url_prefix='/comments')

if __name__ == "__main__":
    app.run(debug=True)
