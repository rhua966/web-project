import time
from flask import Flask

app = Flask(__name__)
app.run(debug=True)



@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/hello/<username>')
def hello(username):
    return f"Hello {username}, thanks for using Flask!"
