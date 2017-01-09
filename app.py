from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth
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

@app.route('/create1/', methods = ['POST'])
def create1():
    if isUser():
        return redirect(url_for('home'))

@app.route('/logout/')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login'))

def isUser():
    if not ('user' in session):
        return False
    return True

if __name__ == '__main__':
    app.debug = True
    app.run()
