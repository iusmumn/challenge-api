import db
import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """A base endpoint just because"""
    return 'Hello, from Challenge API!'

@app.route('/health')
def health():
    """A health endpoint to check if the api is running"""
    return 'Ok!!!'

@app.route('/users')
def users():
    """A users endpoint to grad user data from the database"""
    print("Grabbing user data from database")
    conn = db.connect()
    users = db.get_users(conn)
    return json.dumps(users)
    """return 'test'"""

if __name__ == '__main__':
    app.run()