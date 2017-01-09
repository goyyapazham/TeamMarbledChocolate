import hashlib, sqlite3

def hashPass(password):
    return hashlib.sha512(password).hexdigest()

def register(user, password, gender, bio, movie_keys, ac_keys):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if (userExists(user, c)):
        return ['User already exists.', False]
    elif not user.isalnum() or not password.isalnum():
        return ['Username and password may only consist of alphanumeric characters.', False]
    else:
        p = hashPass(password)
        c.execute("INSERT INTO USERS VALUES ('%s', '%s')"%(user, p))
        bd.commit()
        bd.close()
        return ['Registration successful.', False]

def login(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if not userExists(data[0], c):
        return ['Username does not exist.', False]
    else:
        s = c.execute("SELECT PASSWORD FROM USERS WHERE USERNAME = '%s'" %(data[0]))
        p = s.fetchone()[0]
        if (p != hashPass(data[1])):
            result = ['Incorrect password.', False]
        else:
            result = ['Login successful.', True, data[0]]
    return result

def userExists(username, c):
    s = c.execute("SELECT USERNAME FROM USERS")
    for r in s:
        if username == r[0]:
            return True
    return False
