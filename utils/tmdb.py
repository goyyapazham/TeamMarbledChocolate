import json
import urllib2

f = open("../tmdb.txt", "r")
key = f.read().strip()
f.close()

def read_json(url):
    return json.loads(urllib2.urlopen(url).read())

### GET SUGGESTIONS GIVEN QUERY
# wrapper fxn to use in app.py
def get_suggestions(query):
    #construct API request
    url = "http://api.themoviedb.org/3/search/movie?api_key=%s&query=%s&page=1"%(key, query.replace(" ", "%20"))
    j = read_json(url)

    #error handling: API error
    try:
        if j['status_code'] == 7:
            return "Whoops! The API key didn't work."
    except:
        return titles(get_ids(j))

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
    titles = []
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
            titles += [title]
    return titles

### MATCH BASED ON ARRAYS OF MOVIES LISTED ON PROFILE
def match(p1, p2):
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

#helper
def add_to_score(L1, L2, x):
    i = 0
    for val in L1:
        if val in L2:
            i += x
    return i

#helper
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

#helper
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

#TEST match
print match([4951, 508, 9603], [18785, 64688]) 
