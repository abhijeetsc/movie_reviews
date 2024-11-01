# from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(150), unique=True, nullable=False) 
    email = db.Column(db.String(150), unique=True, nullable=False) 
    password = db.Column(db.String(256), nullable=False)

    def encrypt_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return f'<User {self.user_name}>'