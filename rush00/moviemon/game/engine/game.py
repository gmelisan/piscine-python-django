from moviemon.settings import \
    GRID_SIZE, PLAYER_INIT_X, PLAYER_INIT_Y, \
    MOVIEBALLS_INIT, MOVIEMON_ENCOUNTER_RATE

import pickle
import random

import requests
import json

def init_moviemon(dict_moviemon):
    """инициируем мувимона из словаря апи в наш словарь с нужными полями"""
    moviemon = dict()
    dict_params = {
        "name" : "Title",
        "id" : "imdbID",
        "stranght" : "imdbRating",
        "date" : "Released",
        "director" : "Director",
        "writer" : "Writer",
        "image" : "Poster",
    }
    for key in dict_params:
        moviemon[key] = dict_moviemon[dict_params[key]]
        # moviemon.setdefault(key, []).append(dict_moviemon[dict_params[key]]) (если значений больше чем один)
    moviemon['catched'] = False
    return(moviemon)

def create_moviemons():
    list_moviemons = list()
    list_id_movie = [
        "tt0060666",
        "tt0463392",
        "tt0803096",
        "tt1333125",
        "tt0120616",
        "tt0062453",
        "tt0078748",
        "tt0198781",
        "tt1740707",
        "tt0034398",
    ]
    for id_movie in list_id_movie:
        json_moviemon = requests.get("http://www.omdbapi.com/?i=" + id_movie + "&apikey=7d498d06")
        list_moviemons.append(init_moviemon(json_moviemon.json()))
        #print(moviemon, "\n")
    return(list_moviemons)


class Cell:
    data = ''
    # contains either:
    # '', 'movieball', 'moviemon'
    player = False # player in this cell?
    
    def __init__(self, data='', player=False):
        self.data = data
        self.player = player
    def __str__(self):
        return self.data

class Game:
    """Core class with game logic"""

    pos_x = 0
    pos_y = 0
    movieballs = 0
    m = [] # map, list of lists of Cell
    message = ''
    moviemons = []
    
    def __init__(self):
        #self.load_default_settings()
        pass
    
    def load(self, data):
        """data is packed info about game - position, movieballs count..."""
        self.pos_x = data['x']
        self.pos_y = data['y']
        self.movieballs = data['movieballs']
        self.message = data['msg']
        self.moviemons = data['moviemons']
        self.m = []
        m_str = data['m']
        for i in range (0, GRID_SIZE[0]):
            self.m.append([])
            for j in range(0, GRID_SIZE[1]):
                self.m[i].append(Cell(data=m_str[i][j]))
        
        self.m[self.pos_y][self.pos_x].player = True
        

    def dump(self):
        # pack data to dict for pickle
        data = {
            'msg': self.message,
            'x': self.pos_x,
            'y': self.pos_y,
            'movieballs': self.movieballs,
            'moviemons': self.moviemons,
        }
        m_str = []
        for i in range (0, GRID_SIZE[1]):
            m_str.append([])
            for j in range(0, GRID_SIZE[0]):
                m_str[i].append(str(self.m[i][j]))
        data['m'] = m_str
        return data

    def get_random_movie(self):
        i = random.randrange(len(self.moviemons))
        return self.moviemons[i]['id']

    def load_default_settings(self):
        self.pos_x = PLAYER_INIT_X
        self.pos_y = PLAYER_INIT_Y
        self.movieballs = MOVIEBALLS_INIT
        self.m = []
        for i in range (0, GRID_SIZE[1]):
            self.m.append([])
            for j in range(0, GRID_SIZE[0]):
                self.m[i].append(Cell())


        self.m[self.pos_y][self.pos_y] = Cell(player=True)

        try:
            self.moviemons = create_moviemons()
        except Exception:
            self.moviemons = []
        #print(moviemons)
        

        # generate N movieballs randomly
        # generate M moviemons randomly

        self.m[4][3].data = 'movieball'

    def get_strength(self):
        pass

    def get_movie(self):
        pass

    def move(self, x_shift, y_shift):
        #print('move', x_shift, y_shift)
        #print('BEFORE MOVE player count:', self.count_player())
        #print('rm player', self.pos_y, self.pos_x)
        #print('player pos:', self.m[self.pos_y][self.pos_x])
        self.m[self.pos_y][self.pos_x].player = False
        self.pos_x += x_shift
        self.pos_y += y_shift
        if (self.pos_y < 0):
            self.pos_y = 0
        if (self.pos_x < 0):
            self.pos_x = 0
        if (self.pos_y >= GRID_SIZE[1]):
            self.pos_y = GRID_SIZE[1] - 1
        if (self.pos_x >= GRID_SIZE[0]):
            self.pos_x = GRID_SIZE[0] - 1
        #print('----player count:', self.count_player())
        #print('set player', self.pos_y, self.pos_x)
        self.m[self.pos_y][self.pos_x].player = True        
        #print('AFTER MOVE player count:', self.count_player())
        #print('player pos:', self.m[self.pos_y][self.pos_x])
        if self.get_current() == 'movieball':
            self.clear_current()
            self.movieballs += 1
            self.message = 'Found movieball!'
        else:
            if self.moviemon_encounter():
                self.message = 'Wild moviemon appeared!'
                return True
            else:
                self.message = ''
            
        return False

    def get_current(self):
        return self.m[self.pos_y][self.pos_x].data
    
    def clear_current(self):
        self.m[self.pos_y][self.pos_x].data = ''

    def moviemon_encounter(self):
        if (random.random() <= MOVIEMON_ENCOUNTER_RATE):
            return True
        return False
        
