import jwt
from functools import wraps
from config import Config
from user.models import User
from flask_restful import abort

def authenticate(func):
    @wraps(func)
    def decorated(*args, **kwargs):
            if not func.__self__.argument["token_sign_in"]:
                 return "No se provee el token", 403
            try:
                token = func.__self__.argument["token_sign_in"]
                data = jwt.decode(token, Config.SECRET_KEY, algorithms=["HS256"])
                kwargs["user"] = User.query.get(data['public_id'])
                return func(*args, **kwargs)
            except:
                 return "No tiene privilegios para acceder a este servico", 403                 
    return decorated