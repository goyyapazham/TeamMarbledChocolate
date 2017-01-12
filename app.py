from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth
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
        return render_template('login.html', message = data[0])

@app.route('/create1/')
def create1():
    if isUser():
        return redirect(url_for('home'))
    return render_template('create1')

@app.route('/register/', methods = ['POST'])
def register(number):
    if isUser():
        return redirect(url_for('home'))
    if number == 1:
        data = [request.form['username'], request.form['password'], request.form['gender']]
        auth.register2(data)
    elif number == 2:
        data = [request.form['movie_keys']]
        auth.register1(data)
    else:
        data = [request.form['ac_keys']]
        auth.register3(data)



@app.route('/logout/')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login'))

def isUser():
    if not ('user' in session):
        return False
    return True
##ELY TESTING STUFF NOT THAT RELEVANT BUT SORTA RELEVANT
@app.route('/elytest/')
def elytest():
    return render_template('elytest.html');

@app.route('/process/', methods = ['POST'])
def process():
    d=request.form['text']
    #PROCESS(d): (backend)
    d+="ELYBEST"
    ret = []
    ret.append(d)
    d+="1"
    ret.append(d)
    d+="2"
    ret.append(d)
    #^^TO BE REPLACED BY PROCESS WHICH RETURNS LIST OF SUGGESTIONS
    ret = {'results':ret}
    print ret
    return json.dumps(ret);

if __name__ == '__main__':
    app.debug = True
    app.run()
