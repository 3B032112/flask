from flask import Flask,render_template,request
app = Flask(__name__,template_folder='templates',static_url_path='/static',static_folder='static')
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
@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

if __name__ =='__main__':
    app.run()