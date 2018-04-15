#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.box import Box
"""Tiles"""
class tile:
    def __init__(self, typ, obj, location):
        self.type = typ
        self.obj = obj
        self.box = None
        self.location = location
    
    def check_live(self, box):
        for child in box.location:
            if child == self.location:
                if self.type == 0 and self.obj != None:
                        if self.obj.symbol == "$":
                            return True
                elif self.type == 2 and len(box.location) == 2:
                    return True
                elif self.type == 1: 
                    return True
        return False

    def get_location(self):
        return self.location
    
    def set_box(self, box):
        self.box = box
    
    def set_obj(self, obj):
        self.obj = obj