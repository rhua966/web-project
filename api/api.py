import time
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort


app = Flask(__name__)
api = Api(app)

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required")
video_put_args.add_argument("likes", type=int, help="Likes of the video is required")
videos = {}

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
