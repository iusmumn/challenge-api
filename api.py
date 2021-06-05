import db
import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """A base endpoint just because"""
    return 'Hello, from Challenge API!'

if __name__ == '__main__':
    app.run()