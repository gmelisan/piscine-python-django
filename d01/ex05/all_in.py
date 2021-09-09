import sys

def find_by_key(d, key):
    for k in d.keys():
        if (k.lower() == key.lower()):
            return d[k]

def find_by_value(d, value):
    for k, v in d.items():
        if (v.lower() == value.lower()):
            return k

def start():
    states = {
        "Oregon"   : "OR",
        "Alabama"  : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }

    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    items = sys.argv[1].split(",")
    for i in items:
        i = i.strip()
        if (i == ""):
            continue
        if i.lower() in (x.lower() for x in states.keys()):
            code = find_by_key(states, i)
            print(capital_cities[code] + " is the capital of " + find_by_value(states, code))
        elif i.lower() in (x.lower() for x in capital_cities.values()):
            code = find_by_value(capital_cities, i)
            state = find_by_value(states, code)
            print(capital_cities[code] + " is the capital of " + state)
        else:
            print(i + " is neither a capital city nor a state")
          
if __name__ == '__main__':
    if (len(sys.argv) == 2):
        start()
