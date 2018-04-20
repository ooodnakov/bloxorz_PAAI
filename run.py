#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Run"""
import pygame
from model.solver import *
from drawing.display import Display
from copy import deepcopy
from model.map import maps

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
    

def draw_path(solution, display, timesleep=0.5, level=Level.lv0):
    if solution != None:
        choiselv = maps(level)

        level = Control(choiselv)
        level.draw_StartBox()
        level.draw_StartMaps()
        display.update() 

        time.sleep(timesleep)
        for path in solution:
            level.current = path[0]
            level.update_box_locaton_for_maps(path[0])
            level.maps.refreshBox()
            level.update_current_location()

            level.draw_box()
            level.draw_maps()   
            display.update()

            time.sleep(timesleep)
        return
    else:
        print("No Solution!")
    
def main(level=Level.lv0, Play_handle=True, algorithm=Algorithm.DFS):
    pygame.init()
    Maps = maps(level)
    display = Display(title='Bloxorz Game', map_size=(Maps.size[0], Maps.size[1]))
    state = Control(Maps)

    if Play_handle:
        state.Play_handle = Play_handle
        handle(state, display)
    else:
        if algorithm == Algorithm.DFS:
            result = dfs_path(state)
            draw_path(result, display, level=level)
        elif algorithm == Algorithm.BFS:
            result = bfs_path(state)
            draw_path(result, display, level=level)
        elif algorithm == Algorithm.HILL:
            pass

    time.sleep(10)
    return

if __name__=="__main__":
    main(level=Level.lv11, Play_handle=False, algorithm=Algorithm.BFS)