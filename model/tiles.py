#!/usr/bin/env python
# -*- coding: utf-8 -*-
from model.box import Box
"""Tiles"""
class tile:
    def __init__(self, typ, obj, location):
        self.type = typ
        self.obj = obj
        self.location = location
    
    def check_material_tile(self, box):
        for child in box.location:
            if child == self.location:
                # Space
                if self.type == 0 and self.obj != None:
                        if self.obj.symbol == "$":
                            return True
                # Orange
                elif self.type == 2 and not box.is_standing():
                    return True
                # Rock
                elif self.type == 1: 
                    return True
        return False

    def get_location(self):
        return self.location
    
    # def set_box(self, box):
    #     self.box = box
    
    def set_obj(self, obj):
        self.obj = obj