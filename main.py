from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__) #our main object
api = Api(app) #main entry point of our application

video_put_args = reqparse.RequestParser() #automatically parse through the request and fits our guidlines
video_put_args.add_argument("name", type=str, help="Name of the video")
video_put_args.add_argument("likes", type=int, help="Number of likes of the video")
video_put_args.add_argument("views", type=int, help="Views of the video")
videos = {}

class Video(Resource): #A class that inherits a resource. Allows us to override methods from the Resource such as GET, PUT, POST, etc. 
    def get(self, video_id):
        return videos.get(video_id) #Using dictionary to make it JSON serializable as JSON has a key value pair format
    
    def post(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return "Put Successful"
    
    def delete(self, video_id):
        videos.pop(video_id)
        return "Delete Successful"
    
    def patch(self, video_id):
        args = video_put_args.parse_args()
        videos[video_id] = args
        return "Patch Successful"
#Registers the helloworld resource to the api. This resource is accessible via the URL /video
api.add_resource(Video,"/video/<int:video_id>") #angle brackets to pass in arguments type:name

if __name__ == "__main__":
    app.run(debug=True) #runs the application at localhost, debug = True wil automatically reload after code changes