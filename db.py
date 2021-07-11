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
        user_dict = db_row_to_dict_user(row)
        users.append(user_dict)
    return users

def db_row_to_dict_user(row: tuple) -> dict:
    """Helper function to convert a tuple of data into a dict
    row: tuple of user data
    Returns:
    A dict with db columns as the dict keys
    """
    column_names = [
            "id", "username", "password", "name", 
            "email", "challenge_id", "points", "role"
        ]
    return dict(zip(column_names, list(row)))

def get_challenges(conn):
    """Grab a list of challenges from the database.
    Arguments:
    conn: psycopg2.extensions.connection object
    Returns:
    A list of python dicts containing challenge data
    """
    challenges = []
    cur = conn.cursor()
    cur.execute('SELECT * FROM challenges;')
    for row in cur.fetchall():
        challenge_dict = db_row_to_dict_challenge(row)
        challenges.append(challenge_dict)
    return challenges
    return dict(zip(column_names, list(row)))

def db_row_to_dict_challenge(row: tuple) -> dict:
    """Helper function to convert a tuple of data into a dict
    row: tuple of user data
    Returns:
    A dict with db columns as the dict keys
    """
    column_names = [
            "id", "challenge_id", "name", "status", 
            "leader", "start_date", "end_date"
        ]
    return dict(zip(column_names, list(row)))