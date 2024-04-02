from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'
@app.route('/about')
def about():
    return '<h1>Here could be something about me</h1>'