from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth, tmdb
import json

app = Flask(__name__)
app.secret_key = 'pineapples'

@app.route('/')
def root():
    if not isUser():
        return redirect(url_for('login'))
    return redirect(url_for('home'))

@app.route('/home/')
def home():
    if not isUser():
        return redirect(url_for('login'))
    return render_template('home.html', user = session['user'])

@app.route('/login/')
def login():
    if isUser():
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/authenticate/', methods = ['POST'])
def authenticate():
    data = [request.form['username'], request.form['password']]
    data = auth.login(data)
    if data[1]:
        session['user'] = data[2]
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login', message = data[0]))

@app.route('/create1/<message>/')
def create1(message):
    if isUser():
        return redirect(url_for('home'))
    return render_template('create1.html', message = message)

@app.route('/create2/')
def create2():
    return render_template('login.html')

@app.route('/register/', methods = ['POST'])
def register():
    if isUser():
        return redirect(url_for('home'))
    number = request.form['number']
    if int(number) == 1:
        data = [request.form['username'], request.form['password'], request.form['uGender'], request.form['tGender']]
        data = auth.register1(data)
        if bool(data[1]):
            return redirect(url_for('create2'))
        else:
            return redirect(url_for('create1', message = data[0]))
    elif int(number) == 2:
        data = [request.form['movie_keys']]
        data = auth.register2(data)
        return redirect(url_for('create3'))
    else:
        data = [request.form['ac_keys']]
        data = auth.register3(data)
        return redirect(url_for('home'))

@app.route('/logout/')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login', message = 'Hope to see you soon!'))

def isUser():
    if not ('user' in session):
        return False
    return True

@app.route('/suggest/', methods = ['POST'])
def process():
    d=request.form['text']
    ret = tmdb.get_suggestions(d)
    ret = {'results':ret}
    return json.dumps(ret);

if __name__ == '__main__':
    app.debug = True
    app.run()
