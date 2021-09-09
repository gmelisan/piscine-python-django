import sys
import requests
from bs4 import BeautifulSoup

def get_page(name):
    name = name.replace(' ', '_')
    url = 'https://en.wikipedia.org/wiki/' + name
    #print('requst to', url)
    r = requests.get(url)
    r.raise_for_status()
    return r.text

def has_brackets(s):
    return (s[0] == '[' and s[len(s) - 1] == ']')

def parse_page(page):
    soup = BeautifulSoup(page, 'html.parser')
    title = soup.title.string
    content = soup.find_all(class_="mw-parser-output")
    paragraphs = content[0].find_all('p', class_='')
    for p in paragraphs:
        for tag in p.find_all('a'):
            if isinstance(tag.string, str):
                #print('check link', tag.string)
                if not has_brackets(tag.string):
                    #print('has no brackets')
                    if (tag.previous_sibling == None or
                            (tag.previous_sibling != None and
                             tag.previous_sibling.name != 'i')):
                        #print('return')
                        if tag['href'].startswith('/wiki/'):
                            return tag['href'].replace('/wiki/', '')
    raise Exception('It leads to a dead end!')

def start():
    assert(len(sys.argv) == 2), "Expected 1 parameter"
    title = sys.argv[1]
    visited = [title]
    while title.lower() != 'philosophy':
        #print(title)
        next_title = parse_page(get_page(title))
        if (next_title in visited):
            print(visited, next_title)
            raise Exception('It leads to an infinite loop!')
        visited.append(next_title)
        title = next_title
    for site in visited:
        print(site.replace('_', ' '))
    if len(visited) == 1:
        print('1 road from {} to philosophy'.format(sys.argv[1]))
    else:
        print('{} roads from {} to philosophy'.format(len(visited), sys.argv[1]))
    

if __name__ =='__main__':
    try:
        start()
    except Exception as e:
        print(e)
    #start()
