#MOD 9.4.3
from flask import Flask

app = Flask(__name__)

#Create routes
@app.route('/')
def hello_world():
    return 'Hello world'