from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

@app.route('/')
def movie():
    return "Hey Flask"

if __name__ == '__main__':
    app.run(debug = True)