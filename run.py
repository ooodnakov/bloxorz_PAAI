#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run"""
from model.map import maps
from model.sw import swO, swQ, swX
from model.bridge import Bridge
import os

def logic(maps_object):
    while 1:
        number = input("Nhap Buoc Di:")
        if number == "5":
            maps_object.current_box.move_up()
            res = maps_object.refreshBox()
            if res == False:
                print("GAME OVER!")
                break
        elif number == "2":
            maps_object.current_box.move_down()
            res = maps_object.refreshBox()
            if res == False:
                print("GAME OVER!")
                break
        elif number == "1":
            maps_object.current_box.move_left()
            res = maps_object.refreshBox()
            if res == False:
                print("GAME OVER!")
                break
        elif number == "3":
            maps_object.current_box.move_right()
            res = maps_object.refreshBox()
            if res == False:
                print("GAME OVER!")
                break
        os.system('cls')
        maps_object.print_current()
        if maps_object.check_win():
            print("WINNER!")
            break
    
if __name__=="__main__":
    test =  maps("./level/demo2.json")
    test.print_current()
    logic(test)

