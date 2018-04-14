"""Box"""
class Box:
    def __init__(self, symbol, state, location):
        self.symbol = symbol
        self.state = state
        self.active = False
        self.location = location

    def change_state(self):
        pass

    def move_up(self, maps):
        pass
    
    def move_right(self, maps):
        pass
    
    def move_left(self, maps):
        pass

    def move_down(self, maps):
        pass
    
    def get_locaton(self):
        return self.location

    def on(self):
        self.active = True

    def off(self):
        self.active = False
