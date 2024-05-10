
from flask_restful import Resource, reqparse, fields, marshal_with
from models import *

video_put_args = reqparse.RequestParser() #automatically parse through the request and fits our guidlines
video_put_args.add_argument("name", type=str, help="Name of the video")
video_put_args.add_argument("likes", type=int, help="Number of likes of the video")
video_put_args.add_argument("views", type=int, help="Views of the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource): #A class that inherits a resource. Allows us to override methods from the Resource such as GET, PUT, POST, etc. 
    @marshal_with(resource_fields) #serializes the VideoModel instance into something we can return
    def get(self, video_id):
        result = VideoModel.query.get(video_id)
        return result #Using dictionary to make it JSON serializable as JSON has a key value pair format
    
    @marshal_with(resource_fields)
    def post(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id,name=args['name'],views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video,201