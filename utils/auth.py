import hashlib, sqlite3, shutil
import tmdb
import os
import commands
import cgi, cgitb

def hashPass(password):
    return hashlib.sha512(password).hexdigest()

def register(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    data[0] = data[0].lower()
    if (userExists(data[0], c)):
        return False
    elif not data[0].isalnum() or not data[1].isalnum():
        return False
    elif not data[1] == data[2]:
        return False
    else:
        hash = hashPass(data[2])
        #0=user
        #1,2=pw
        #3=gender
        #4=pref
        #5,6,7=movs
        #8,9,10=images (will implement later)
        mov = [ data[5], data[6], data[7] ]
        img = [ data[8], data[9], data[10] ]
        c.execute("INSERT INTO users VALUES('%s', '%s', '%s', '%s', '%d', '%d', '%d', '%d', '%d', '%d', '%d')"%(data[0], data[1], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], tmdb.comp_mov(mov, mov) + tmdb.comp_img(img, img)))
        tmdb.commit(data[0])
    bd.commit()
    bd.close()

def login(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    data[0] = data[0].lower()
    if not userExists(data[0], c):
        return [False]
    else:
        s = c.execute("SELECT pw FROM USERS WHERE user = '%s'" %(data[0]))
        print s
        p = s.fetchone()[0]
        print p
        if (p != hashPass(data[1])):
            result = [False]
        else:
            result = [True, data[0]]
    bd.commit()
    bd.close()
    #shutil.move('%s.jpg', 'data') %(data[0])
    return result

def userExists(username, c):
    s = c.execute("SELECT USER FROM USERS")
    for r in s:
        if username == r[0]:
            return True
    return False

def profile(user):
        cgitb.enable()
        blah = cgi.FieldStorage()
        try:
            filedata = blah['upload']
        except Exception, e:
            return
        if filedata.file:
            with file('%s.jpg', 'w') %(request.form['user']) as outfile:
                outfile.write(filedata.file.read())
