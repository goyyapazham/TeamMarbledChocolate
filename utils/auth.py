import hashlib, sqlite3

def hashPass(password):
    return hashlib.sha512(password).hexdigest()

def register1(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if (userExists(data[0], c)):
        return ['Username already exists, ya reprobate', False]
    elif not data[0].isalnum() or not data[1].isalnum():
        return ['Username and password may only consist of alphanumeric characters. Prick...', False]
    else:
        hash = hashPass(data[1])
        c.execute("INSERT INTO USERS VALUES ('%s', '%s', '%s', '%s', Null, Null, NUll, Null, Null)" %(data[0], hash, data[2], data[3]))
        return [None, True]
    bd.commit()

def login(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if not userExists(data[0], c):
        return ["I'm afraid to say that username does not exist", False]
    else:
        s = c.execute("SELECT PASSWORD FROM USERS WHERE USERNAME = '%s'" %(data[0]))
        p = s.fetchone()[0]
        if (p != hashPass(data[1])):
            result = ['Looooser! Incorrect password', False]
        else:
            result = [None, True, data[0]]
    return result

def userExists(username, c):
    s = c.execute("SELECT USERNAME FROM USERS")
    for r in s:
        if username == r[0]:
            return True
    return False
