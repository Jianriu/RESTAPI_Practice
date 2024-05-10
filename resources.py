
from sqlalchemy.exc import IntegrityError
from flask_restful import Resource, reqparse, fields, marshal_with, abort
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
        if result is None:
            abort(404, message="Video ID " + str(video_id) + " does not exist.")
        return result #Using dictionary to make it JSON serializable as JSON has a key value pair format
    
    @marshal_with(resource_fields)
    def post(self, video_id):
        args = video_put_args.parse_args()
        video = VideoModel(id=video_id,name=args['name'],views=args['views'], likes=args['likes'])
        try:
            db.session.add(video)
            db.session.commit()
        except IntegrityError as ie:
            db.session.rollback()
            abort(400,message="Video already exists")
        else:
            return video,201

    @marshal_with(resource_fields) 
    def delete(self, video_id):
        result = VideoModel.query.get(video_id)
        if result is None:
            abort(404, message="Video ID " + str(video_id) + " does not exist.")
        else:
            db.session.delete(result)
            db.session.commit()
            return result, 200