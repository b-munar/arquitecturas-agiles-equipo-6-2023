from database import db
from flask_bcrypt import generate_password_hash, check_password_hash
from enum import IntEnum

class TypeUser(IntEnum):
    operator = 1
    seller = 2
    customer = 3


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    type_user = db.Column(db.Integer, default=TypeUser.operator)
    photos = db.relationship('Photo', backref='user')

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf-8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)