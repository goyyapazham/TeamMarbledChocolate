import json
import urllib2

f = open("tmdb.txt", "r")
key = f.read().strip()
f.close()

def read_json(url):
    return json.loads(urllib2.urlopen(url).read())

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

def get_ids(j):
    #limit number of results to 4
    ids = []
    for res in j['results']:
        ids += [res['id']]
    if len(ids) < 4:
        return ids
    else:
        return ids[:4]

def titles(ids):
    titles = []
    for id in ids:
        url = "http://api.themoviedb.org/3/movie/%d?api_key=%s&language=en-US"%(id, key)
        j = read_json(url)
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
'''
#TEST THINGS
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
