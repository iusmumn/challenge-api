from api import tasks
import db_config as config
import psycopg2

def connect():
    """Initiate a postgres database connection using psycopg2
    Returns:
    A psycopg2.extensions.connection object
    """
    return psycopg2.connect(
        dbname = config.dbname,
        user = config.dbuser,
        password = config.dbpassword,
        host = config.dbhost,
        port = '5432'
    )

def get_users(conn):
    """Grab a list of users from the database.

    Arguments:
    conn: psycopg2.extensions.connection object

    Returns:
    A list of python dicts containing user data
    """
    users = []
    cur = conn.cursor()
    cur.execute('SELECT * FROM users;')
    for row in cur.fetchall():
        user_dictionary = db_row_to_dict_user(row)
        users.append(user_dictionary)        
    return users

def get_teams(conn):
    """Grab a list of temas from the database."""
    """initiate a new list of teams"""
    teams = []
    """interact with database"""
    cur = conn.cursor()
    cur.execute('SELECT * FROM teams;')
    """what we fetch is sloppy, so we do a for loop to manipualte each row"""
    for row in cur.fetchall():
        team_dictionary = db_row_to_dict_team(row)
        teams.append(team_dictionary)

    return teams

def get_tasks(conn):
    """Grab a list of tasks from the database."""
    """initiate a new list of tasks"""
    tasks = []
    """interact with database"""
    cur = conn.cursor()
    cur.execute('SELECT * FROM tasks;')
    """what we fetch is sloppy, so we do a for loop to manipualte each row"""
    for row in cur.fetchall():
        task_dictionary = db_row_to_dict_task(row)
        tasks.append(task_dictionary)
        
    return tasks

def db_row_to_dict_user(row: tuple) -> dict:
    """Helper function to convert a tuple of data into a dict

    Arguments:
    row: tuple of user data

    Returns:
    A dict with db columns as the dict keys
    """
    column_names = [
            "id", "username", "password", "name", 
            "email", "challenge_id", "points", "role"
    ]
    return dict(zip(column_names, list(row)))

def db_row_to_dict_team(row: tuple) -> dict:
    """Helper function to convert a tuple of data into a dict
    row: tuple of team data
    Returns:
    A dict with db columns as the dict keys
    """
    column_names = [
            "id", "name", "points" 
            ]
    return dict(zip(column_names, list(row)))

def db_row_to_dict_task(row: tuple) -> dict:
    """Helper function to convert a tuple of data into a dict
    row: tuple of task data
    Returns:
    A dict with db columns as the dict keys
    """
    column_names = [
            "id", "task_id", "challenge_id", "name", "owner",
            "status", "points"
            
        ]
    return dict(zip(column_names, list(row)))



