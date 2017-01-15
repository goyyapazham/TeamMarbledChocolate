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
    #c.execute("INSERT INTO '%s' VALUES ('%s', '%s')" %(getChat(data), data[0], data[2]))
    c.execute("INSERT INTO 'knob-pickle' VALUES ('pickle', 'hey')")
    bd.commit()
    return True

def getChat(data):
    data = sorted(data[:2], key=str.lower)
    return data[0] + '-' + data[1]

def chatExists(data, c):
    s = c.execute("SELECT * FROM sqlite_master WHERE type = 'table' AND name = '%s'" %(getChat(data)))
    for r in s:
        return True
    return False

def getMessages(data):
    bd = sqlite3.connect('data/bd.db')
    c = bd.cursor()
    messages = OrderedDict()
    s = c.execute("SELECT * FROM '%s'" %(getChat(data)))
    for r in s:
        messages [r[0]] = r[1]
    return messages


data = ['pickle', 'knob', 'hey']
startChat(data)
message(data)
texts = getMessages(data)
for i in texts:
    print (texts[i])
