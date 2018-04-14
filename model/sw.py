"""Switch"""

# from model.bridge import Bridge
from model.box import Box

class swQ:
    """Switch Bat Giac"""
    def __init__(self, symbol, typ, active, location, bridge=None):
        self.symbol = symbol
        self.type = typ
        self.active = active
        self.location = location
        self.bridge = bridge
    
    def set_bridge(self, bridge):
        self.bridge = bridge

    def change_active(self):
        self.active = not self.active
        # active lien tuc
        if self.type == 0: 
            self.bridge.change_active()
        else:
        # active chi mot lan duy nhat
            if self.bridge.times_active == 0:
                self.bridge.change_active()
            else: pass
    
    def get_location(self):
        return self.location

    def set_map(self, map):
        pass
            
class swX:
    """Switch X"""
    def __init__(self, symbol, typ, active, location, bridge=None):
        self.symbol = symbol
        self.type = typ
        self.active = active
        self.location = location
        self.bridge = bridge
    
    def set_bridge(self, bridge):
        self.bridge = bridge

    def change_active(self, box=None):
        self.active = not self.active
        # active lien tuc
        if self.type == 0: 
            self.bridge.change_active()
        else:
            # active chi mot lan duy nhat
            if self.bridge.times_active == 0:
                self.bridge.change_active()
            else: pass

    def get_location(self):
        return self.location

    def set_map(self, map):
        pass


class swO:
    """Switch tach doi"""
    def __init__(self, symbol, location, split, box1=None, box2=None):
        self.symbol = symbol
        self.location = location
        self.split = split
        self.box1 = box1
        self.box1 = box2
        self.active = 1
    
    def set_box1(self, symbol, state, location):
        self.box1 = Box(symbol, state, location)

    def set_box2(self, symbol, state, location):
        self.box2 = Box(symbol, state, location)

    def change_active(self):
        if self.active != 1:
            self.active == 1
            self.box1.on()
            self.box2.off()
        else: 
            self.active = 2
            self.box2.on()
            self.box1.off()

    def get_active_box(self):
        if self.active == 1:
            return self.box1
        else: return self.box2

    def get_all_box(self):
        return (self.box1, self.box2)

    def get_location(self):
        return self.location

    def set_map(self, map):
        pass








    

    

