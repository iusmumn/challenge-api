from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """A base endpoint just because"""
    return 'Hello, from Challenge API!'
    
def ren():
    "ren test"
    return 'Hi, Ren is here'

if __name__ == '__main__':
    app.run()