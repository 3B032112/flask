from flask import Flask,render_template, request
app = Flask(__name__,template_folder='templates',static_url_path='/static',static_folder='static')
name = ''
@app.route('/')
@app.route('/index',methods=['GET'])
def index():
    name = request.args.get('name')
    return render_template('index.html',**locals())
@app.route('/shopping')
def shopping():
    return render_template('shopping.html')
@app.route('/tickets')
def tickets():
    return render_template('tickets.html')
@app.route('/welfare')
def welfare():
    return render_template('welfare.html')
@app.route('/user/<username>')
def user(username):
    global name
    name = username
    return render_template('user.html',name=username)
@app.route('/search',methods=['GET','POST'])
def search():
    global name
    username = name
    if request.method == 'GET':
        message = 'please use post method'
        return render_template('result.html', message=message)
    keyword = request.form['keyword']
    if keyword=='red':
        message = 'is red'
    elif keyword == 'yellow':
        message = 'is yellow'
    elif keyword == 'green':
        message = 'is green'
    else:
        message = 'not found'
    return render_template('user.html',name=username,message=message)

if __name__ =='__main__':
    app.run()