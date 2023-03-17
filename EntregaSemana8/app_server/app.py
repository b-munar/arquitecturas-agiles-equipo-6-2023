from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate

from user.controllers import Signup, Signin
from photo.controllers import UploadPhoto, Photo

from config import Config
from database import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

api = Api(app)


api.add_resource(UploadPhoto, '/upload-photo')
api.add_resource(Photo, '/photo')
api.add_resource(Signup, '/signup')
api.add_resource(Signin, '/signin')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=4000)