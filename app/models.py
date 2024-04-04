# models.py

from app import app 
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt

db = SQLAlchemy(app)
bcrypt = Bcrypt()

class Credentials(db.Model):
    __tablename__ = "credentials"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(55), nullable=False)


    def set_password(self, password):  # class user_data in user_password using 
        self.password = bcrypt.generate_password_hash(password).decode("utf-8") #       

    def check_password(self, password): # class user_data in user_password using check a password
        return bcrypt.check_password_hash(self.password,password)
    
    def update_profile(self, username, email):
        self.username = username
        self.email = email
        db.session.commit()

    def __repr__(self):
        return f"Credentials(id={self.id}, username={self.username}, email={self.email})"
    

    
