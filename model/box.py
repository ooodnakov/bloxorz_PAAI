"""Box"""
class Box:
    def __init__(self, symbol, state, location):
        self.symbol = symbol
        self.state = state
        self.active = False
        self.location = location

    def change_state(self):
        pass
    
    def get_locaton(self):
        return self.location

    def on(self):
        self.active = True

    def off(self):
        self.active = False
