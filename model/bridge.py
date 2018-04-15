#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bridge"""

class Bridge:
    def __init__(self, symbol, active, location):
        self.symbol = symbol
        self.times_active = 0
        self.active = active
        self.location = location
        self.type = len(location)

    def check_times_active(self):
        if self.times_active > 0:
            return True
        else: return False
    
    def change_active(self):
        self.active = not self.active
        self.times_active += 1
        
