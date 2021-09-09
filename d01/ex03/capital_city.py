import sys

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
    if sys.argv[1] not in states:
        print("Unknown state")
        return
    code = states[sys.argv[1]]
    print(capital_cities[code])

if __name__ == '__main__':
    if (len(sys.argv) == 2):
        start()
