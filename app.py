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
    data = [request.form['user'], request.form['password']]
    data = auth.login(data)
    if bool(data[0]):
        session['user'] = data[1]
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

@app.route('/create/', methods = ['POST'])
def create():
    if isUser():
        return redirect(url_for('home'))
    data = [request.form['user'], request.form['email'], request.form['p1'], request.form['p2'], request.form['gender'], request.form['pref'], request.form['security'], request.form['m0'], request.form['m1'], request.form['m2'], request.form['i0'], request.form['i1'], request.form['i2'], request.form['bio']]
    if auth.register(data):
        return redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('login'))

def isUser():
    if not ('user' in session):
        return False
    return True

@app.route('/suggest/', methods = ['POST'])
def process():
    d=request.form['text']
    #send ids thru form
    ret = tmdb.get_suggestions(d)
    #ids = tmdb.get_ids(d)
    #ret = tmdb.get_suggestions(ids)
    ret = {'results':ret}
    return json.dumps(ret)

@app.route('/images/', methods = ['POST'])
def images():
    ret=["big", "small", "floor", "bulkhead", "slim", "fan", "window", "central", "ceilingfan"]
    #makeImages() - randomizes the list. It then uses google images to find the image files
    # and store them in img0.jpg, img1.jpg, .. , img8.jpg where the order is the order of the new randomized list
    # it returns the randomized list
    ret={'results':ret}
    return json.dumps(ret);


if __name__ == '__main__':
    app.debug = True
    app.run()
