from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from models import db
from resources import *
app = Flask(__name__) #our main object
api = Api(app) #main entry point of our application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.db' #configurate where the database for this app will be
db.init_app(app) 

#db.create_all() #only do this once, creates/initializes the database
    
#Registers the helloworld resource to the api. This resource is accessible via the URL /video
api.add_resource(Video,"/video/<int:video_id>") #angle brackets to pass in arguments type:name

if __name__ == "__main__":
    app.run(debug=True) #runs the application at localhost, debug = True wil automatically reload after code changes