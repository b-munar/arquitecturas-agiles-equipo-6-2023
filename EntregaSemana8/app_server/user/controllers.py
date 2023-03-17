
from database import db
from user.models import User
from flask_restful import reqparse, Resource
from flask import jsonify
import jwt
from datetime import datetime, timedelta
from config import Config
from authorizer import authenticate

parser_user = reqparse.RequestParser()
parser_user.add_argument('username', type=str)
parser_user.add_argument('password', type=str)

class Signup(Resource):
    def post(self):
        args = parser_user.parse_args()
        new_user = User(
            username=args['username'],
            password=args['password']
        )
        new_user.hash_password()
        db.session.add(new_user)
        db.session.commit()
        return args

class Signin(Resource):
    def post(self):
        args = parser_user.parse_args()
        user = User.query.filter_by(username=args['username']).first()
        if user.check_password(args['password']):
            token_sign_in = jwt.encode({
                        'public_id': user.id,
                        'exp' : datetime.utcnow() + timedelta(minutes = 30)
                    }, Config.SECRET_KEY, algorithm="HS256")
            return jsonify({'token_sign_in': token_sign_in})
        