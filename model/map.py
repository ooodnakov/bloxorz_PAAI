"""Map"""
import simplejson as json
from model.sw import swO, swQ, swX
from model.box import Box
from model.bridge import Bridge
from model.tiles import tile

class maps:
    def __init__(self, path_to_level=None):
        self.files = None
        self.jsonObj = None
        self.maps = list()
        self.level = None
        self.size = None
        self.start = None
        self.end = None 
        self.current_box = None
        self.types_tile = None
        self.swQ = list()
        self.swX = list()
        self.swO = list()
        self.Brid = list()
        if path_to_level != None:
            self.loadLevel(path_to_level)

    def loadLevel(self, path_to_level=None):
        if path_to_level != None:
            self.files = open(path_to_level, "r")
            self.jsonObj = json.loads(self.files.read())

            # Name Level
            self.level = self.jsonObj["level"]
            # Size Map
            self.size = self.jsonObj["size"]
            # Start Location
            self.start = self.jsonObj["start"]
            # End Location
            self.end = self.jsonObj["end"]
            # Types of tiles
            self.types_tile = [self.jsonObj["tiles"]["orange"], self.jsonObj["tiles"]["rock"], self.jsonObj["tiles"]["space"]]
            # Current Box
            boxObj = self.jsonObj["box"]
            self.current_box = Box(boxObj["symbol"], boxObj["state"], boxObj["location"])
            # Load swX
            self.__loadSWX()
            # Load swQ
            self.__loadSWQ()
            # Load swO
            self.__loadSWO()
            # Load Maps
            self.__loadMap()

        else: print("Path_to_level not None")
    
    def __loadMap(self):
        maps = self.jsonObj["maps"]
        for i in range(self.size[0]):
            line = []
            for j in range(self.size[1]):
                if maps[i][j] == self.types_tile[0]: # orange tile
                    newtile = tile(2, None, [i, j])
                    line.append(newtile)
                elif maps[i][j] == self.types_tile[1]: # rock tile
                    newtile = tile(1, None, [i, j])
                    line.append(newtile)
                elif maps[i][j] == self.types_tile[2]: # space title
                    newtile = tile(0, None, [i, j])
                    line.append(newtile)
                else:
                    newtile = tile(1, None, [i, j])
                    line.append(newtile)
            self.maps.append(line)
        
        if len(self.swO) != 0:
            for one in self.swO:
                gettile = self.maps[int(one.location[0])][int(one.location[1])]
                gettile.set_obj(one)
                self.maps[int(one.location[0])][int(one.location[1])] = gettile
        if len(self.swQ) != 0:
            for one in self.swQ:
                gettile = self.maps[int(one.location[0])][int(one.location[1])]
                gettile.set_obj(one)
                self.maps[int(one.location[0])][int(one.location[1])] = gettile
        if len(self.swX) != 0:
            for one in self.swX:
                gettile = self.maps[int(one.location[0])][int(one.location[1])]
                gettile.set_obj(one)
                self.maps[int(one.location[0])][int(one.location[1])] = gettile
        if len(self.Brid) != 0:
            for one in self.Brid:
                if one.type == 1:
                    gettile = self.maps[int(one.location[0][0])][int(one.location[0][1])]
                    gettile.set_obj(one)
                    self.maps[int(one.location[0][0])][int(one.location[0][1])] = gettile
                elif one.type == 2:
                    gettile = self.maps[int(one.location[0][0])][int(one.location[0][1])]
                    gettile.set_obj(one)
                    self.maps[int(one.location[0][0])][int(one.location[0][1])] = gettile
                    gettile = self.maps[int(one.location[1][0])][int(one.location[1][1])]
                    gettile.set_obj(one)
                    self.maps[int(one.location[1][0])][int(one.location[1][1])] = gettile
        
        # Start Box
        gettile = self.maps[int(self.start[0])][int(self.start[1])]
        gettile.set_obj(self.current_box)
        self.maps[int(self.start[0])][int(self.start[1])] = gettile

                
    def __loadSWX(self):
        swXObj = self.jsonObj["swX"]
        count = int(swXObj["count"])
        if count > 0:
            symbol = swXObj["symbol"]
            for sym in symbol:
                symObj = swXObj[sym]
                newswX = swX(sym, symObj["type"], symObj["active"], symObj["location"])
                bridObj = self.jsonObj["bridge"]
                nameBrid = symObj["bridge"]
                if int(bridObj["count"]) > 0:
                    chidBrid = bridObj[nameBrid]
                    newBrid = Bridge(nameBrid, chidBrid["active"], chidBrid["location"])
                    newswX.set_bridge(newBrid)
                    self.Brid.append(newBrid)
                self.swX.append(newswX)

    def __loadSWQ(self):
        swQObj = self.jsonObj["swQ"]
        count = int(swQObj["count"])
        if count > 0:
            symbol = swQObj["symbol"]
            for sym in symbol:
                symObj = swQObj[sym]
                newswQ = swQ(sym, symObj["type"], symObj["active"], symObj["location"])
                bridObj = self.jsonObj["bridge"]
                nameBrid = symObj["bridge"]
                if int(bridObj["count"]) > 0:
                    chidBrid = bridObj[nameBrid]
                    newBrid = Bridge(nameBrid, chidBrid["active"], chidBrid["location"])
                    newswQ.set_bridge(newBrid)
                    self.Brid.append(newBrid)
                self.swQ.append(newswQ)
    
    def __loadSWO(self):
        swOObj = self.jsonObj["swO"]
        count = int(swOObj["count"])
        if count > 0:
            symbol = swOObj["symbol"]
            for sym in symbol:
                symObj = swOObj[sym]
                newswO = swO(sym, symObj["location"], symObj["split"])
                box1 = symObj["box1"]
                box2 = symObj["box2"]
                newswO.set_box1(box1["symbol"], box1["state"], box1["location"])
                newswO.set_box2(box2["symbol"], box2["state"], box2["location"])
                self.swO.append(newswO)

    def print_current(self):
        for i in self.maps:
            for j in i:
                print(j.type, j.obj)
            print("\n")



    
