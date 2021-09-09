import sys
from antigravity import geohash

def usage(error):
    s = str(error) + '\n'
    s += ('Usage: python3 {0} <latitude> <longitude> <datedow>\n' + \
        'Example: python3 {0} 55.7971244 37.5786924 2021-08-12-35499.71') \
        .format(sys.argv[0])
    return s

def start():
    assert(len(sys.argv) == 4), '3 parameters expected'
    geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode('ascii'))

if __name__ =='__main__':
    try:
        start()
    except Exception as e:
         print(usage(e))
