from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello, World!'
@app.route('/about')
def about():
    return '<h1>Here could be something about me</h1>'
@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>' 
@app.route('/user/<name>/<Surname>')
def post(name, Surname):
    return f'<h1>Hello, {name} {Surname}!</h1>'
if __name__ == '__main__':
    app.run()