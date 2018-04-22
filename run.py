#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Run"""
import pygame
import sys
import os
import time
from model.solver import dfs_path, bfs_path, handle, hill_climbing
from drawing.display import Display
from model.map import maps
from model.control import Control

class Algorithm:
    DFS = 1
    BFS = 2
    HILL= 3

class Level:
    lv0  = "./level/0.json"
    lv1  = "./level/1.json"
    lv10 = "./level/10.json"
    lv11 = "./level/11.json"
    lv12 = "./level/12.json"
    lv13 = "./level/13.json"
    lv14 = "./level/14.json"
    lv15 = "./level/15.json"
    
def deltatime(start_time):
    result = time.time() - start_time
    print("Time: ", result)

def flatMap(path):
    return [y for x in path for y in x]

def draw_path_3D(solution, display, timesleep=0.5, level=Level.lv0):
    if solution != None:
        print("Found solution success!")
        print(solution)
        choiselv = maps(level)

        level = Control(choiselv)
        level.draw_StartBox()
        level.draw_StartMaps()
        display.update() 

        for path in solution:
            time.sleep(timesleep)
            level.current = path
            level.update_box_locaton_for_maps(path)
            
            if level.maps.refreshBox():
                level.update_current_location()
            else: 
                print("Solution Fail!")
                return

            level.draw_box() 
            level.draw_maps()   
            display.update()
        return
    else:
        print("Unable to find path for maps!")
        print("Dir path: %s" % level)
        return

def draw_path_2D(solution, timesleep=0.5, level=Level.lv0):
    if solution != None:
        print("Found solution success!")
        print(solution)
        choiselv = maps(level)

        level = Control(choiselv)
        level.print_maps()
        
        time.sleep(timesleep)

        for path in solution:
            os.system("clear")
            level.current = path
            level.update_box_locaton_for_maps(path)
            level.maps.refreshBox()

            if level.maps.refreshBox():
                level.update_current_location()
            else: 
                print("Solution Fail!")
                return

            level.print_maps()
            time.sleep(timesleep)
        return
    else:
        print("Unable to find path for maps!")
        print("Dir path: %s" % level)
        return
    
def main(level=Level.lv0, Play_handle=True, algorithm=Algorithm.DFS):
    print("Processing...")
    pygame.init()
    Maps = maps(level)
    display = Display(title='Bloxorz Game', map_size=(Maps.size[0], Maps.size[1]))
    state = Control(Maps)

    if Play_handle:
        state.Play_handle = Play_handle
        handle(state, display)
    else:
        Start_Time = time.time()
        if algorithm == Algorithm.DFS:
            result = dfs_path(state)
            deltatime(Start_Time)
            # draw_path_2D(result, level=level)
            draw_path_3D(result, display, level=level)
        elif algorithm == Algorithm.BFS:
            result = bfs_path(state)
            deltatime(Start_Time)
            # draw_path_2D(result, level=level)
            draw_path_3D(result, display, level=level)
        elif algorithm == Algorithm.HILL:
            result = hill_climbing(state)
            deltatime(Start_Time)
            # draw_path_2D(result, level=level)
            draw_path_3D(result, display, level=level)
    time.sleep(3)
    sys.exit()

if __name__=="__main__":
    main(level=Level.lv0, Play_handle=False, algorithm=Algorithm.HILL)

# Chỉnh sửa 
# Level : thay đổi level game
# Play_handle : True nếu muốn chơi tay
# Algorithm : Tên giải thuật tìm kiếm