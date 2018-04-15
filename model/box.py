#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Box"""
class Box:
    def __init__(self, symbol, state, location):
        self.symbol = symbol
        self.state = state
        self.active = False
        self.location = location
        self.pre_location = None

    def change_state(self, state):
        self.state = state

    def move_up(self):
        numGPS = len(self.location)
        if self.state == 2:
            # Nam dung
            if numGPS == 1:
                yi = self.location[0][0]
                xi = self.location[0][1]
                newYi1 = int(yi-1)
                newYi2 = int(yi-2)
                newLocation = [[newYi1, xi],[newYi2, xi]]
                self.change_location(newLocation)
            else:
                # Nam ngang
                if self.check_verti_or_hori() == 0:
                    y1 = self.location[0][0]
                    x1 = self.location[0][1]
                    y2 = self.location[1][0]
                    x2 = self.location[1][1]
                    newY1 = int(y1-1)
                    newY2 = int(y2-1)
                    newLocation = [[newY2, x1], [newY1, x2]]
                    self.change_location(newLocation)
                # Nam Doc
                elif self.check_verti_or_hori() == 1:
                    yi = self.location[1][0]
                    xi = self.location[1][1]
                    newYi = int(yi-1)
                    newLocation = [[newYi, xi]]
                    self.change_location(newLocation)
        elif self.state == 1:
            if numGPS == 1:
                yi = self.location[0][0]
                xi = self.location[0][1]
                newYi = int(yi-1)
                newLocation = [[newYi, xi]]
                self.change_location(newLocation)
    def move_right(self):
        numGPS = len(self.location)
        if self.state == 2:
            # Nam dung
            if numGPS == 1:
                yi = self.location[0][0]
                xi = self.location[0][1]
                newXi1 = int(xi+1)
                newXi2 = int(xi+2)
                newLocation = [[yi, newXi1],[yi, newXi2]]
                self.change_location(newLocation)
            else:
                # Nam ngang
                if self.check_verti_or_hori() == 0:
                    yi = self.location[1][0]
                    xi = self.location[1][1]
                    newXi = int(xi+1)
                    newLocation = [[yi, newXi]]
                    self.change_location(newLocation)
                # Nam Doc
                elif self.check_verti_or_hori() == 1:
                    y1 = self.location[0][0]
                    x1 = self.location[0][1]
                    y2 = self.location[1][0]
                    x2 = self.location[1][1]
                    newX1 = int(x1+1)
                    newX2 = int(x2+1)
                    newLocation = [[y1, newX1],[y2, newX2]]
                    self.change_location(newLocation)
        elif self.state == 1:
            if numGPS == 1:
                yi = self.location[0][0]
                xi = self.location[0][1]
                newXi = int(xi+1)
                newLocation = [[yi, newXi]]
                self.change_location(newLocation)
    def move_left(self):
        numGPS = len(self.location)
        if self.state == 2:
            # Nam dung
            if numGPS == 1:
                yi = self.location[0][0]
                xi = self.location[0][1]
                newXi1 = int(xi-1)
                newXi2 = int(xi-2)
                newLocation = [[yi, newXi2],[yi, newXi1]]
                self.change_location(newLocation)
            else:
                # Nam ngang
                if self.check_verti_or_hori() == 0:
                    yi = self.location[0][0]
                    xi = self.location[0][1]
                    newXi = int(xi-1)
                    newLocation = [[yi, newXi]]
                    self.change_location(newLocation)
                # Nam Doc
                elif self.check_verti_or_hori() == 1:
                    y1 = self.location[0][0]
                    x1 = self.location[0][1]
                    y2 = self.location[1][0]
                    x2 = self.location[1][1]
                    newX1 = int(x1-1)
                    newX2 = int(x2-1)
                    newLocation = [[y1, newX1],[y2, newX2]]
                    self.change_location(newLocation)
        elif self.state == 1:
            if numGPS == 1:
                yi = self.location[0][0]
                xi = self.location[0][1]
                newXi = int(xi-1)
                newLocation = [[yi, newXi]]
                self.change_location(newLocation)

    def move_down(self):
        numGPS = len(self.location)
        if self.state == 2:
            # Nam dung
            if numGPS == 1:
                yi = self.location[0][0]
                xi = self.location[0][1]
                newYi1 = int(yi+1)
                newYi2 = int(yi+2)
                newLocation = [[newYi2, xi],[newYi1, xi]]
                self.change_location(newLocation)
            else:
                # Nam ngang
                if self.check_verti_or_hori() == 0:
                    y1 = self.location[0][0]
                    x1 = self.location[0][1]
                    y2 = self.location[1][0]
                    x2 = self.location[1][1]
                    newY1 = int(y1+1)
                    newY2 = int(y2+1)
                    newLocation = [[newY1, x1], [newY2, x2]]
                    self.change_location(newLocation)
                # Nam Doc
                elif self.check_verti_or_hori() == 1:
                    yi = self.location[0][0]
                    xi = self.location[0][1]
                    newYi = int(yi+1)
                    newLocation = [[newYi, xi]]
                    self.change_location(newLocation)
        elif self.state == 1:
            if numGPS == 1:
                yi = self.location[0][0]
                xi = self.location[0][1]
                newYi = int(yi+1)
                newLocation = [[newYi, xi]]
                self.change_location(newLocation)
    
    def get_locaton(self):
        return self.location
    
    def check_verti_or_hori(self, location=None):
        if location != None:
            if len(location) == 2:
                y1 = location[0][0]
                x1 = location[0][1]
                y2 = location[1][0]
                x2 = location[1][1]
                if y1 == y2:
                    return 0 # Ngang
                if x1 == x2: 
                    return 1 # Doc
        else:
            if len(self.location) == 2:
                y1 = self.location[0][0]
                x1 = self.location[0][1]
                y2 = self.location[1][0]
                x2 = self.location[1][1]
                if y1 == y2:
                    return 0 # Ngang
                if x1 == x2: 
                    return 1 # Doc
            
    def change_location(self, location):
        self.pre_location = self.location
        self.location = location

    def on(self):
        self.active = True

    def off(self):
        self.active = False
