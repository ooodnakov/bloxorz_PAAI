#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tiles"""
class tile:
    def __init__(self, typ, obj, location):
        self.type = typ
        self.obj = obj
        self.location = location
    
    def check(self, box):
        pass
    
    def set_obj(self, obj):
        self.obj = obj