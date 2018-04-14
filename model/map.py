"""Map"""
import simplejson as json

class maps(object):
    def __init__(self, link_path_level=None):
        self.files = None
        self.jsonObject = None
        if link_path_level != None:
            self.loadLevel(link_path_level)
        # print(self.jsonObject["swO"])

    def loadLevel(self, link_path_level=None):
        self.files = open(link_path_level, "r")
        self.jsonObject = json.loads(self.files.read()) 
