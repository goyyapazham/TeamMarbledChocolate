from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth, tmdb, message
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
    else:
        user = session['user']
        messages = message.getRecents(user)
        print messages
        return render_template('home.html', user = user, nummessages = message.getNumberUnread(user), messages=messages)

@app.route('/login/')
def login():
    if isUser():
        return redirect(url_for('home'))
    return render_template('login.html', message = "")

@app.route('/authenticate/', methods = ['POST'])
def authenticate():
    data = [request.form['user'], request.form['password']]
    data = auth.login(data)
    if bool(data[0]):
        session['user'] = data[1]
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))

#This intro loads before loading create
@app.route('/intro/', methods = ['POST'])
def intro():
    user = request.form['user']
    p1 = request.form['p1']
    p2 = request.form['p2']
    gender = request.form['gender']
    pref = request.form['pref']
    movie0 = request.form['movie0']
    movie1 = request.form['movie1']
    movie2 = request.form['movie2']
    i0 = request.form['i0']
    i1 = request.form['i1']
    i2 = request.form['i2']
    return render_template('intro.html', user = user, p1 = p1, p2 = p2, gender = gender, pref = pref, movie0 = movie0, movie1 = movie1, movie2 = movie2, i0=i0, i1=i1, i2=i2, create =1)

#Standard intro
@app.route('/intro2/', methods = ['POST'])
def intro2():
    return render_template('intro.html', user = "", p1 = "", p2 = "", gender = "", pref = "", movie0 = "", movie1 = "", movie2 = "", i0="", i1="", i2="", create = 0)

@app.route('/create/', methods = ['POST'])
def create():
    if isUser():
        return redirect(url_for('home'))
    data = [request.form['user'], request.form['p1'], request.form['p2'], request.form['gender'], request.form['pref'], int(request.form['movie0']), int(request.form['movie1']), int(request.form['movie2']), int(request.form['i0']), int(request.form['i1']), int(request.form['i2'])]
    auth.profile(request.form['user'])
    if auth.register(data):
        return redirect(url_for('login'))
    return redirect(url_for('login'))

@app.route('/logout/', methods = ['POST'])
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
    print ret
    return json.dumps(ret)

@app.route('/match/', methods = ['POST'])
def match():
    user=request.form['user']
    matches = tmdb.all_lovers(user);
    return render_template('match.html', user = user, matches = matches)

@app.route('/startChat/', methods = ['POST'])
def startChat():
    user=request.form['user']
    recip=request.form['recip']
    print "WE GOT UP OT HERE ALL RIGHT"
    message.startChat(user,recip)
    return redirect(url_for('mess', user = user, recip =recip))

@app.route('/mess/', methods = ['GET'])
def mess():
    user=request.args['user']
    recip=request.args['recip']
    messages=message.getMessages(user,recip)
    return render_template('mess.html', user = user, recip = recip, messages=messages)

@app.route('/sendMess/', methods = ['POST'])
def sendMess():
    user=request.form['user']
    recip=request.form['recip']
    text=request.form['text']
    message.message(user,recip,text);
    messages=message.getMessages(user,recip)
    return render_template('mess.html', user = user, recip = recip, messages=messages)

if __name__ == '__main__':
    app.debug = True
    app.run()
