from flask_restful import reqparse, Resource
from photo.models import Photo
from authorizer import authenticate
import pika
import json

parser_upload_photo = reqparse.RequestParser()
parser_upload_photo.add_argument('path', type=str)
parser_upload_photo.add_argument('token_sign_in', type=str)

class UploadPhoto(Resource):
    method_decorators = [authenticate]
    def __init__(self):
        self.argument = parser_upload_photo.parse_args()
    def post(self, **kwargs):
        args = {
            "path": self.argument["path"],
            "user_id": kwargs["user"].id
        }

        try:
            connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq"))
        except pika.exceptions.AMQPConnectionError:
            print("Failed to connect to RabbitMQ service. Photo wont be sent.")
            return
        
        channel = connection.channel()
        channel.queue_declare(queue='photo_queue')

        channel.basic_publish(
            exchange='',
            routing_key='photo_queue',
            body=json.dumps(args),
        )

        return {'path' : args['path']}

class Photo(Resource):
    def get(self):
        Photo.query.all()
        return 0