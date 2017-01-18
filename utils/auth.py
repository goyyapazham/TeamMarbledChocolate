import hashlib, sqlite3

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
        c.execute("INSERT INTO USERS VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(data[0], data[1], hash, data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]))
    bd.commit()

def login(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if not userExists(data[0], c):
        return [False]
    else:
        s = c.execute("SELECT PASSWORD FROM USERS WHERE USERNAME = '%s'" %(data[0]))
        p = s.fetchone()[0]
        if (p != hashPass(data[1])):
            result = [False]
        else:
            result = [True, data[0]]
    return result

def userExists(username, c):
    s = c.execute("SELECT USERNAME FROM USERS")
    for r in s:
        if username == r[0]:
            return True
    return False
