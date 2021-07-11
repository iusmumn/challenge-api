import json
import db
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
    """A users endpoint to grab user data from the database"""
    print("Grabbing users data from databse!")
    conn = db.connect()
    users = db.get_users(conn)
    return json.dumps(users)

@app.route('/challenges')
def challenges():
    """A users endpoint to grab user data from the database"""
    print("Grabbing challenge data from databse!")
    conn = db.connect()
    challenges = db.get_challenges(conn)
    return json.dumps(challenges)

if __name__ == '__main__':
    app.run()