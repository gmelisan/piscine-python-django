import sys

def find_by_value(d, value):
    for k, v in d.items():
        if (v == value):
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
    if sys.argv[1] not in capital_cities.values():
        print("Unknown capital city")
        return
    code = find_by_value(capital_cities, sys.argv[1])
    print(find_by_value(states, code))
          
if __name__ == '__main__':
    if (len(sys.argv) == 2):
        start()
