import requests
import json
import dewiki
import sys


def wikipedia_search(title):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'query',
        'list': 'search',
        'srsearch': title,
        'format': 'json'
    }
    r = requests.get(url, params)
    r.raise_for_status()
    data = json.loads(r.text)
    if 'error' in data.keys():
        raise Exception(data['error']['info'])
    if ('suggestion' in data['query']['searchinfo']):
        return data['query']['searchinfo']['suggestion']
    if (len(data['query']['search']) > 0):
        return data['query']['search'][0]['title']
    return title

def wikipedia_get(title):
    found = wikipedia_search(title)
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        'action': 'parse',
        'page': found,
        'prop': 'wikitext',
        'format': 'json',
        'redirects': 'true'
    }
    r = requests.get(url, params)
    r.raise_for_status()
    data = json.loads(r.text)
    if 'error' in data.keys():
        raise Exception(data['error']['info'])
    return dewiki.from_string(data['parse']['wikitext']['*'])

def start():
    assert(len(sys.argv) == 2), "Expected 1 parameter"
    s = wikipedia_get(sys.argv[1])
    name = sys.argv[1].replace(' ', '_')
    with open(name + '.wiki', 'w') as f:
        f.write(s)
        
if __name__ =='__main__':
    try:
        start()
    except Exception as e:
        print(e)
