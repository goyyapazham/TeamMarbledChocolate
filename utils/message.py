import sqlite3
from collections import OrderedDict

def startChat(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if chatExists(data, c):
        return False
    c.execute("CREATE TABLE '%s' (SENDER TEXT, MESSAGE TEXT)" %(getChat(data)))
    return True

def message(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    if len(data[2]) == 0:
        return False
    c.execute("INSERT INTO '%s' VALUES ('%s', '%s')" %(getChat(data), data[0], data[2]))
    bd.commit()
    return True

def getChat(data):
    data[0] = str(data[0])
    data[1] = str(data[1])
    data = sorted(data[:2], key=str.lower)
    return data[0] + '-' + data[1]

def getUsers(data):
    data = data.split('-')
    return data

def chatExists(data, c):
    s = c.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name = '%s'" %(getChat(data)))
    for r in s:
        return True
    return False

#Returns list of messages in conversatio in tuples
#('Jonathan', 'Hi Ely')
def getMessages(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    messages = []
    s = c.execute("SELECT * FROM '%s'" %(getChat(data)))
    for r in s:
        messages.append((r[0], r[1]))
    return messages

def getChatWithUser(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    chats = []
    s = c.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name LIKE '%s-%%' OR name LIKE '%%-%s'" %(data[0], data[0]))
    for r in s:
        chats.append((r[1]))
    return chats

#Returns list with format: (conversation title, last message in form (sender, content))
#('Ely-Jonathan', ('Jonathan', 'Hi Ely'))
def getRecents(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    chats = getChatWithUser(data)
    recents = []
    for r in chats:
        print r
        messages = getMessages(getUsers(r))
        recents.append((r, messages[-1]))
    return recents
