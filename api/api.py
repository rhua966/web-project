import time
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] - 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    # Define all the fields of the database

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name = {name}, views = {views}, likes = {likes}"

db.create_all() # Only uncomment this line on the first you run it, otherwise data will be replaced everytime server runs 

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required")
video_put_args.add_argument("likes", type=int, help="Likes of the video is required")
# videos = {}

def abort_if_video_doesnt_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video id is not valid...")

def abort_if_video_exist(video_id):
    if video_id in videos:
        abort(409, message="Video with that ID already exists")



class Video(Resource):
    def get(self, video_id):
        abort_if_video_doesnt_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exist(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201

    def delete(self, video_id):
        abort_if_video_doesnt_exist(video_id)
        del videos[video_id]
        return "", 204


api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)



@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/hello/<username>')
def hello(username):
    return f"Hello {username}, thanks for using Flask!"
