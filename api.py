import db
import json

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """A base endpoint just because"""
    return 'Hello, this is the root (or base) endpoint!'

@app.route('/health')
def health():
    """A health endpoint to check if the api is running"""
    return 'OK'

@app.route('/users')
def users():
    """A user endpoint to grab user data from the database"""
    print("Grabbing user data from the database...")
    conn = db.connect()
    users = db.get_users(conn)
    return json.dumps(users)

@app.route('/teams')
def teams():
    """A team endpoint to grab team data from the database"""
    print("Grabbing team data from the database...")
    conn = db.connect()
    teams = db.get_teams(conn)
    return json.dumps(teams)

@app.route('/tasks')
def tasks():
    """A team endpoint to grab task data from the database"""
    print("Grabbing task data from the database...")
    conn = db.connect()
    tasks = db.get_tasks(conn)
    return json.dumps(tasks)
@app.route('/challenges')
def challenges():
    """A challenges endpoint to grab challenge data from the datapages"""
    print("Grabbing challenge data from database")
    conn = db.connect()
    challenges = db.get_challenges(conn)
    return json.dumps(challenges)

if __name__ == '__main__':
    app.run()