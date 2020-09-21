import time, uuid, sys, os
import sqlite3
from flask import Flask, send_file, g, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
# from flask_sqlalchemy import SQLAlchemy

DATA_ROOT = os.path.dirname(os.path.abspath(__file__)) + "/Data"

app = Flask(__name__)
api = Api(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATA_ROOT + "/Data.db")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


# class VideoModel(db.Model):
#     # Define all the fields of the database

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     views = db.Column(db.Integer, nullable=False)
#     likes = db.Column(db.Integer, nullable=False)

#     def __repr__(self):
#         return f"Video(name = {name}, views = {views}, likes = {likes}"

# db.create_all() # Only uncomment this line on the first you run it, otherwise data will be replaced everytime server runs 

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

# resouce_fields = {
#     'id': fields.Integer,
#     'name': fields.String,
#     'views': fields.Integer,
#     'likes': fields.Integer
# }

# class Video(Resource):

#     @marshal_with(resouce_fields)
#     def get(self, video_id):
#         result = VideoModel.query.filter_by(id=video_id).first()
#         if not result:
#             abort(404, message="Could not find video with that ID...")

#         # Serizelize result using resource_fields
#         return result

#     @marshal_with(resouce_fields)
#     def put(self, video_id):
#         args = video_put_args.parse_args()
#         result = VideoModel.query.filter_by(id=video_id).first()
#         if result:
#             abort(409, message='Video id taken...')
#         video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
#         db.session.add(video)
#         db.session.commit()
#         return video, 201


    # def delete(self, video_id):
    #     abort_if_video_doesnt_exist(video_id)
    #     del videos[video_id]
    #     return "", 204
class Items(Resource):
    def get(self):
        with app.app_context():
            cur = get_db().cursor()
            cur.execute("SELECT * FROM Items;")
            r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
            return r

class ItemImages(Resource):
    def get(self):
        imgid = request.args.get("id")
        path = DATA_ROOT + f"/Images/{imgid}.jpg"
        
        if os.path.isfile(path):
            return send_file(path, "image/jpeg")
        else:
            return send_file(DATA_ROOT + f"/Images/Default.png", "image/png")


class Version(Resource):
    def get(self):
        return "1.0.0"

class ID(Resource):
    def get(self):
        return str(uuid.uuid4())

class VCard(Resource):
    def get(self):
        return send_file(DATA_ROOT + "/contact.vcf", "text/x-vcard")

# api.add_resource(Video, "/video/<int:video_id>")
api.add_resource(Items, "/items")
api.add_resource(ItemImages, "/itemimg")
api.add_resource(Version, "/version")
api.add_resource(ID, "/id")
api.add_resource(VCard, "/vcard")


if __name__ == "__main__":
    app.run(debug=True)



@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/hello/<string:username>')
def hello(username):
    return f"Hello {username}, thanks for using Flask!"
