#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import time
from model.control import Control
from model.map import maps
from model.control import Control
from drawing.display import Display
from drawing.box import Box
import pygame

def print_stack(stack, algorithm):
    if algorithm=="dfs":
        print("STACK: ")
        for state in stack[::-1]:
            print("( %s ) " % state)
    elif algorithm=="bfs":
        print("QUEUE: ")
        for state in stack:
            print("( %s ) " % state)

def dfs(state: Control):
    while state.stack:
        current_state = state.stack.pop()
        current_maps = state.stack_maps.pop()
        for move in state.moves:
            state.set_state(current_state, current_maps)
            if move():
                if state.check_goal():
                    return

def dfs_recursion(state: Control):
    if state.check_goal():
        return
    current_state = state.stack.pop()
    current_maps = state.stack_maps.pop()
    for move in state.moves:
        state.set_state(current_state, current_maps)
        if move():
            dfs_recursion(state)

def bfs(state: Control):
    while state.stack:
        current_state = state.stack.pop(0)
        current_maps = state.stack_maps.pop(0)
        for move in state.moves:
            state.set_state(current_state, current_maps)
            if move():
                if state.check_goal():
                    return

def dfs_step_by_step(state: Control, timesleep=0.5, display=None):
    while state.stack:
        current_state = state.stack.pop()
        current_maps = state.stack_maps.pop()

        print("POP: ( %s )" % current_state)

        for move in state.moves:
            state.set_state(current_state, current_maps)

            print_stack(state.stack, "dfs")
            state.maps.print_current()
            state.draw_maps()
            state.draw_box()
            display.update()

            time.sleep(timesleep)
            os.system("clear")
            if move():
                print_stack(state.stack, "dfs")
                state.maps.print_current()

                time.sleep(timesleep)
                if state.check_goal():
                    print("WINNER!")
                    return state, display

            os.system("clear")
            state.draw_maps()
            state.draw_box()
            display.update()

def bfs_step_by_step(state: Control, timesleep=0.5, display=None):
    while state.stack:
        current_state = state.stack.pop(0)
        current_maps = state.stack_maps.pop(0)

        print("POP: ( %s )" % current_state)

        for move in state.moves:
            state.set_state(current_state, current_maps)

            print_stack(state.stack, "bfs")
            state.maps.print_current()
            state.draw_maps()
            state.draw_box()
            display.update()

            time.sleep(timesleep)
            os.system("clear")
            if move():
                
                print_stack(state.stack, "bfs")
                state.maps.print_current()
                time.sleep(timesleep)

                if state.check_goal():
                    print("WINNER!")
                    return state, display
                    
            os.system("clear")
            state.draw_maps()
            state.draw_box()
            display.update()

def dfs_path(state: Control):
    stack = [[state.current], ]
    stack_maps = [[state.start_maps], ]
    while state.stack:
        current_state = state.stack.pop()
        current_maps = state.stack_maps.pop()
        path = stack.pop()
        path_maps = stack_maps.pop()
        for move in state.moves:
            state.set_state(current_state, current_maps)
            if move():
                if state.check_goal():
                    result1 = path + [state.current]
                    result2 = path_maps + [state.curr_maps]
                    return [(c,t) for c, t in zip(result1, result2)] 
                stack.append(path + [state.current])
                stack_maps.append(path_maps + [state.curr_maps])

def bfs_path(state: Control):
    stack = [[state.current], ]
    stack_maps = [[state.start_maps], ]
    while state.stack:
        current_state = state.stack.pop(0)
        current_maps = state.stack_maps.pop(0)
        path = stack.pop(0)
        path_maps = stack_maps.pop(0)
        for move in state.moves:
            state.set_state(current_state, current_maps)
            if move():
                if state.check_goal():
                    result1 = path + [state.current]
                    result2 = path_maps + [state.curr_maps]
                    return [(c,t) for c, t in zip(result1, result2)] 
                stack.append(path + [state.current])
                stack_maps.append(path_maps + [state.curr_maps])

    
def hill_climbing(state: Control):
    pass

def handle(state: Control, display):
    result = True
    while True:
        os.system("clear")
        for event in pygame.event.get():
            if state.Play_handle:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    result = state.move_up()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    result = state.move_down()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    result = state.move_right()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    result = state.move_left()
            else: pass
                
            if display.quit(event):
                return
        state.draw_maps()
        state.draw_box()
        state.print_maps()
        display.update()

        if state.check_goal():
            print("WINNER!")
            return
        if result == False:
            print("LOSER!")
            return