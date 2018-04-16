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
                if self.type == 0:
                    if self.obj != None:
                        if self.obj.symbol == "$":
                            return True
                        else: return False
                    else: return False
                # Orange
                elif self.type == 2:
                    if not box.is_standing():
                        return True
                    else: return False
                # Rock
                elif self.type == 1: 
                    return True

    def get_location(self):
        return self.location
    
    def set_obj(self, obj):
        self.obj = obj