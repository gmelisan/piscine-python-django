import pickle

class StateManager:
    filename = 'gamestate'

    def save(self, data):
        with open(self.filename, 'wb') as f:
            pickle.dump(data, f)
            print('data saved')
        
    def load(self):
        try:
            with open(self.filename, 'rb') as f:
                data = pickle.load(f)
                print('data loaded')
        except FileNotFoundError:
            return None
        return data
