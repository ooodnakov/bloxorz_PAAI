#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run"""
from model.map import maps
from model.sw import swO, swQ, swX
from model.bridge import Bridge
import os

def dfs(maps_object):
    pass

def bfs(maps_object):
    pass

def hill_climbing(maps_object):
    pass

def handle(maps_object):
    result = True
    while 1:
        number = input("Nhap Buoc Di:")
        if number == "5":
            maps_object.current_box.move_up()
        elif number == "2":
            maps_object.current_box.move_down()
        elif number == "1":
            maps_object.current_box.move_left()
        elif number == "3":
            maps_object.current_box.move_right()
        
        result = maps_object.refreshBox()

        if result == False:
            print("GAME OVER!")
            break
        os.system('clear')
        maps_object.print_current()
        if maps_object.check_goal():
            print("WINNER!")
            break
    
if __name__=="__main__":
    level =  maps("./level/demo2.json")
    level.print_current()
    handle(level)

