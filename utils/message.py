import sqlite3
from collections import OrderedDict
from random import randint

def startChat(user, recip):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if chatExists(user, recip, c):
        return False
    c.execute("CREATE TABLE '%s' (SENDER TEXT, MESSAGE TEXT)" %(getTitle(user, recip)))
    message(user, recip, randomPickUpLine())
    return True

def randomPickUpLine():
    pickUps = []
    pickUps.append('Hey gurl, wanna see my air-conditioner?')
    pickUps.append('Wanna come to my house and see if you can turn on my air-conditioner too?')
    pickUps.append('Is that an air-conditioner in your pants or are you just glad to see me?')
    pickUps.append('Is it just me or do we need an air-conditioner in here?')
    pickUps.append("You must not have an air-conditioner, becasue I'm your fan and you're turning me on")
    return pickUps[randint(0,4)]

def message(user, recip, text):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if len(text) == 0:
        return False
    c.execute("INSERT INTO '%s' VALUES ('%s', '%s')" %(getTitle(user, recip), user, text))
    bd.commit()
    return True

def getTitle(user, recip):
    l = [user, recip]
    title = sorted(l)
    return title[0] + '-' + title[1]

def getUsers(title):
    users = title.split('-')
    return users

def getNumberUnread(user):
    unread = 0
    recents = getRecents(user)
    for r in recents:
        if r[1][0] != user:
            unread += 1
    return unread

def chatExists(user, recip, c):
    s = c.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name = '%s'" %(getTitle(user, recip)))
    for r in s:
        return True
    return False

def notMatched(user):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    unmatched = []
    s = c.execute('SELECT * FROM USERS')
    for r in s:
        if not chatExists(user, r, c):
            unmatched.append(r)
    return unmatched

#Returns list of messages in conversatio in tuples
#('Jonathan', 'Hi Ely')
def getMessages(user, recip):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    messages = []
    s = c.execute("SELECT * FROM '%s'" %(getTitle(user, recip)))
    for r in s:
        messages.append((r[0], r[1]))
    return messages

def getTitleWithUser(user):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    chats = []
    s = c.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name LIKE '%s-%%' OR name LIKE '%%-%s'" %(user, user))
    for r in s:
        r = getUsers(r[1])
        t = (r[0], r[1])
        chats.append(t)
    return chats

#Returns list with format: (conversation title, last message in form (sender, content))
#('Ely-Jonathan', ('Jonathan', 'Hi Ely'))
def getRecents(user):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    chats = getTitleWithUser(user)
    recents = []
    for r in chats:
        print r[0]
        print r[1]
        messages = getMessages(r[0], r[1])
        title = getTitle(r[0], r[1])
        try:
            recents.append((title, messages[-1]))
        except IndexError:
            recents = []
    return recents
