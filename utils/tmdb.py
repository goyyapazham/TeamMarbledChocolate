import json
import urllib2
import sqlite3

f = open("tmdb.txt", "r")
key = f.read().strip()
f.close()

def read_json(url):
    return json.loads(urllib2.urlopen(url).read())

### GET SUGGESTIONS GIVEN QUERY
# wrapper fxn to use in app.py
def get_suggestions(query):
#def get_suggestions(ids): - removed to debug
    #construct API request
    url = "http://api.themoviedb.org/3/search/movie?api_key=%s&query=%s&page=1"%(key, query.replace(" ", "%20"))
    j = read_json(url)

    #error handling: API error
    try:
        if j['status_code'] == 7:
            return "Whoops! The API key didn't work."
    except:
        return titles(get_ids(j))
        #return titles(ids)

# helper fxn for get_suggestions
def get_ids(j):
    #limit number of results to 4
    ids = []
    for res in j['results']:
        ids += [res['id']]
    if len(ids) < 4:
        return ids
    else:
        return ids[:4]

# helper fxn for get_suggestions
def titles(ids):
    titles = {}
    for id in ids:
        j = read_json("http://api.themoviedb.org/3/movie/%d?api_key=%s&language=en-US"%(id, key))
        try:
            if j['status_code'] == 7:
                return "Whoops! The API key didn't work."
        except:
            title = j['original_title']
            try:
                title = str(title)
            except:
                pass
            titles[id]=title
    return titles

### MATCH BASED ON ARRAYS OF MOVIES LISTED ON PROFILE
# WILL return user2's compatibility with user1 (i.e., how much user1 should want to go out w user2

def all_lovers(user):

    L = []

    db = sqlite3.connect("data/bd.db")
    c = db.cursor()

    c.execute("SELECT user FROM users")
    u = c.fetchall()

    db.close()

    for i in range(len(u)):
        lol = str(u[i][0])
        if lol != user:
            L += [ [lol, compatibility(user, lol)] ]

    return L
        

# helper
def compatibility(user1, user2):

    db = sqlite3.connect("data/bd.db")
    c = db.cursor()

    c.execute("SELECT mov1, mov2, mov3 FROM users WHERE user == \"%s\""%(user1))
    mov1 = c.fetchall()[0]
    c.execute("SELECT mov1, mov2, mov3 FROM users WHERE user == \"%s\""%(user2))
    mov2 = c.fetchall()[0]

    c.execute("SELECT img1, img2, img3 FROM users WHERE user == \"%s\""%(user1))
    img1 = c.fetchall()[0]
    c.execute("SELECT img1, img2, img3 FROM users WHERE user == \"%s\""%(user2))
    img2 = c.fetchall()[0]
    
    c.execute("SELECT max FROM users WHERE user == \"%s\""%(user1))
    u1max = c.fetchall()[0][0]

    db.close()

    mov = comp_mov(mov1, mov2)
    img = comp_img(img1, img2)

    return comp(mov, img, u1max)

# helper
def comp(mov, img, umax):
    return round( ((mov + img) * 1.0 / umax * 100), 2 )

# helper
def comp_img(p1, p2):

    comp = 0
    
    for val in p1:
        if val in p2:
            comp += 10

    return comp

# helper
def comp_mov(p1, p2):
    sim1 = []
    sim2 = []
    gen1 = []
    gen2 = []
    for id in p1:
        j = read_json("https://api.themoviedb.org/3/movie/%d/similar?api_key=%s&language=en-US&page=1"%(id, key))
        try:
            if j['status_code'] == 7:
                return "Whoops! The API key didn't work."
        except:
            gen1 = add_no_dup(gen1, get_genres(id))
            for res in j['results']:
                newid = int(res['id'])
                sim1 += [newid]
    for id in p2:
        j = read_json("https://api.themoviedb.org/3/movie/%d/similar?api_key=%s&language=en-US&page=1"%(id, key))
        try:
            if j['status_code'] == 7:
                return "Whoops! The API key didn't work."
        except:
            gen2 = add_no_dup(gen2, get_genres(id))
            for res in j['results']:
                newid = int(res['id'])
                sim2 += [newid]
    
    return add_to_score(p1, p2, 5) + add_to_score(sim1, sim2, 2) + add_to_score(gen1, gen2, 1)

#helper fxn for match
def add_to_score(L1, L2, x):
    i = 0
    for val in L1:
        if val in L2:
            i += x
    return i

#helper fxn for match
def get_genres(movieid):
    j = read_json("https://api.themoviedb.org/3/movie/%d?api_key=%s&language=en-US"%(movieid, key))
    try:
        if j['status_code'] == 7:
            return "Whoops! The API key didn't work."
    except:
        ret = []
        genres = j['genres']
        for res in genres:
            ret += [int(res['id'])]
    return ret

#helper fxn for match
def add_no_dup(existing, new):
    for val in new:
        if val not in existing:
            existing += [val]
    return existing

'''
#TEST get_suggestions
#10 things i hate about you
print get_suggestions("10")
print get_suggestions("10 things")
#love actually
print get_suggestions("l")
print get_suggestions("love")
print get_suggestions("love a")
#good will hunting
print get_suggestions("good")
print get_suggestions("good will")
'''

'''
#TEST compatibility lol
mov1 = [4951, 489, 508]
mov2 = [4951, 489, 9603]
img1 = [3, 4, 7]
img2 = [2, 3, 7]

#print comp(comp_mov(mov1, mov2), comp_img(img1, img2), 168)
#print compatibility("nala", "nala")
#print compatibility("nala", "nalala")

#print all_lovers("nala")
#print all_lovers("nalala")
'''
