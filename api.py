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

if __name__ == '__main__':
    app.run()