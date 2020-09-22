import time, uuid, sys, os, hashlib
import sqlite3
from flask import Flask, send_file, g, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_httpauth import HTTPTokenAuth
# from flask_sqlalchemy import SQLAlchemy

DATA_ROOT = os.path.dirname(os.path.abspath(__file__)) + "/Data"

app = Flask(__name__)
api = Api(app)
auth = HTTPTokenAuth(scheme="Digest", realm="Dairy")

# Connection to the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATA_ROOT + "/Data.db")
    return db

class Items(Resource):
    def get(self):

        db = get_db()
        with db:
            cur = db.cursor()
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
post_comment_args = reqparse.RequestParser()
post_comment_args.add_argument("Name", str)
post_comment_args.add_argument("Comment", str)

class Comment(Resource):

    def get(self):
        db = get_db()
        with db:
            cur = db.cursor()
            cur.execute("SELECT * FROM Comments;")
            r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()] 
        return r, 200

    def post(self):
        args = post_comment_args.parse_args()
        name = args['Name']
        comment = args['Comment']

        db = get_db()
        with db:
            cur = db.cursor()
            cur.execute("INSERT INTO Comments (Name, Comment) VALUES (?, ?);", (name, comment))

        return f"Comment ({comment}) posted from user ({name}).", 201
        # return "Comment Submitted", 201



post_args_parser = reqparse.RequestParser()
post_args_parser.add_argument("Username", str)
post_args_parser.add_argument("Password", str)

class Register(Resource):
    
    def post(self):
        # print(request.data)
        # json_data = request.get_json(force=True)
        args = post_args_parser.parse_args()
        username = args['Username']
        password = args['Password']
        hashed_password = hashlib.md5(f"{username}:{password}".encode()).hexdigest()
        db = get_db()
        with db:
            cur = db.cursor()

            if (cur.execute("SELECT * FROM 'Credentials' WHERE User = ?", [username]).fetchone() is None):
                # Username available
                cur.execute("INSERT INTO 'Credentials' (User, Password) VALUES (?, ?);", [username, hashed_password])
                return f"User {username} registered.", 201
            else:
                # Username already exists
                return f"User {username} already exists, please try another one.", 404

        # cur.close()
users = {
    "Kyle": "1",
    "Huang": "2"
}


class Login(Resource):

    @auth.get_password
    def get_pwd(self, username):
        if username in users:
            return users.get(username)
        return None

    @auth.login_required
    def get(self):
        return f"Hello, {auth.username()}!"

class Version(Resource):
    def get(self):
        return {"version": "1.0.0"}

class ID(Resource):
    def get(self):
        return {"uuid": str(uuid.uuid4())}

class VCard(Resource):
    def get(self):
        return send_file(DATA_ROOT + "/contact.vcf", "text/x-vcard")

api.add_resource(Items, "/api/items")
api.add_resource(ItemImages, "/api/itemimg")
api.add_resource(Comment, "/api/comment")
api.add_resource(Register, "/api/register")
api.add_resource(Login, "/api/login")
api.add_resource(Version, "/api/version")
api.add_resource(ID, "/api/id")
api.add_resource(VCard, "/api/vcard")


if __name__ == "__main__":
    app.run(debug=True)

@app.route('/api/')
def index():
    return "Flask is running!"

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/api/hello/<string:username>')
def hello(username):
    return f"Hello {username}, thanks for using Flask!"
