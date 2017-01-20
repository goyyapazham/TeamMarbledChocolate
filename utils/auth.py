import hashlib, sqlite3
import tmdb

def hashPass(password):
    return hashlib.sha512(password).hexdigest()

def register(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if (userExists(data[0], c)):
        return False
    elif not data[0].isalnum() or not data[2].isalnum():
        return False
    elif not data[2] == data[3]:
        return False
    else:
        hash = hashPass(data[2])
        #0=user
        #1=email
        #2,3=pw
        #4=gender
        #5=pref
        #6=security
        #7,8,9=movs
        #10,11,12=images (will implement later)
        #13=bio
        mov = [ int(data[7]), int(data[8]), int(data[9]) ]
        c.execute("INSERT INTO users VALUES(%s, %s, %s, %s, %s, %s, %d, %d, %d, %d, %s)"%(data[0], data[1], data[2], data[4], data[5], data[6], int(data[7]), int(data[8]), int(data[9]), tmdb.match(mov, mov), data[13])) #WILL INCLUDE OTHER THINGS LATER
    bd.commit()
    bd.close()

def login(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if not userExists(data[0], c):
        return [False]
    else:
        s = c.execute("SELECT P1 FROM USERS WHERE USER = '%s'" %(data[0]))
        p = s.fetchone()[0]
        if (p != hashPass(data[1])):
            result = [False]
        else:
            result = [True, data[0]]
    bd.commit()
    bd.close()
    return result

def userExists(username, c):
    s = c.execute("SELECT USER FROM USERS")
    for r in s:
        if username == r[0]:
            return True
    return False
