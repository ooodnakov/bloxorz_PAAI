#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import time
from model.control import Control
from model.map import maps
from drawing.display import Display
from drawing.box import Box
from model.box import Box as cube
import pygame
from copy import deepcopy
from heapq import heappop, heappush, heapify

def print_stack(stack, algorithm):
    if algorithm=="dfs":
        print("STACK: ")
        for state in stack[::-1]:
            print("( %s ) " % state[0])
    elif algorithm=="bfs":
        print("QUEUE: ")
        for state in stack:
            print("( %s ) " % state[0])


def dfs_recursion(state: Control):
    if state.check_goal():
        return
    current_state = state.sdfs_pathtack.pop()
    current_maps = state.stack_maps.pop()
    state.visted.append((current_state, current_maps))
    for move in state.moves:
        state.set_state(current_state, current_maps)
        if move():
            dfs_recursion(state)


def dfs_step_by_step(state: Control, timesleep=0.1):
    pygame.init()
    display = Display(title='Bloxorz Game', map_size=(state.size[0], state.size[1]))

    while state.stack:
        current_state, current_maps = state.stack.pop()
        
        print("POP: ( %s )" % current_state)
        
        state.visted.append((current_state, current_maps))

        for move in state.moves:
            state.set_state(current_state, current_maps)

            print_stack(state.stack, "dfs")
            state.maps.print_current()
            state.draw_box()
            state.draw_maps()
            display.update()
            time.sleep(timesleep)
            os.system("clear")

            if move():
                print_stack(state.stack, "dfs")
                state.maps.print_current()
                time.sleep(timesleep)
                os.system("clear")
                if state.check_goal():
                    print("WINNER!")
                    state.maps.print_current()
                    state.draw_box()
                    state.draw_maps()
                    display.update()
                    time.sleep(timesleep)
                    return state
        os.system("clear")
        

def bfs_step_by_step(state: Control, timesleep=0.2):
    pygame.init()
    display = Display(title='Bloxorz Game', map_size=(state.size[0], state.size[1]))

    while state.stack:
        current_state, current_maps = state.stack.pop(0)

        print("POP: ( %s )" % current_state)

        state.visted.append((current_state, current_maps))

        for move in state.moves:
            state.set_state(current_state, current_maps)

            print_stack(state.stack, "bfs")
            state.maps.print_current()
            state.draw_box()
            state.draw_maps()
            display.update()
            time.sleep(timesleep)
            os.system("clear")

            if move():
                print_stack(state.stack, "bfs")
                state.maps.print_current()
                time.sleep(timesleep)
                os.system("clear")
                if state.check_goal():
                    print("WINNER!")
                    state.maps.print_current()
                    state.draw_box()
                    state.draw_maps()
                    display.update()
                    time.sleep(timesleep)
                    return state
                    
            os.system("clear")

def dfs_path(state: Control):
    stack = [[state.start], ]
    while state.stack:
        current_state, current_maps = state.stack.pop()
        path = stack.pop()
        state.visted.append((current_state, current_maps))
        for move in state.moves:
            state.set_state(current_state, current_maps)
            if move():
                if state.check_goal():
                    result = path + [state.current]
                    return result 
                stack.append(path + [state.current])
                
    return None

def bfs_path(state: Control):
    stack = [[state.start], ]
    while state.stack:
        current_state, current_maps = state.stack.pop(0)
        path = stack.pop(0)
        state.visted.append((current_state, current_maps))
        for move in state.moves:
            state.set_state(current_state, current_maps)
            if move():
                if state.check_goal():
                    result = path + [state.current]
                    return result
                stack.append(path + [state.current])
                
    return None

    
def hill_climbing(state: Control,verbose=None):
    state.eval_func()
    if verbose:
        print("Eval_Maps")
        print(state.eval_maps)
    count = 0
    path = [] 
    all_accept_state = []
    best_state = []

    while True:
        current_state = state.get_state()
        current_maps = state.get_maps()
        current_eval = state.evaluate()

        path.append(current_state)
        accept_state = []

        state.visted.append((current_state, current_maps))

        for move in state.moves:
            if move():
                delta = state.evaluate()
                if delta <= current_eval:
                    better_state = state.get_state()
                    get_maps = state.get_maps()
                    accept_state.append((delta, better_state, get_maps))
                
            state.set_state(current_state, current_maps)
                  
        if accept_state != []:
            next_eval, next_state, next_maps = min(accept_state)
            best_state.append(next_state)
            all_accept_state.extend(sorted(accept_state))

            if next_state == state.end:
                path.append(next_state)
                return path

            state.set_state(next_state, next_maps)
        else: 
            try:
                count +=1
                if verbose:
                    print("Try again!", count)
                    print(path)
                while True:
                    next_eval, next_state, next_maps = all_accept_state.pop()
                    if next_state in best_state:
                        path.pop()
                        continue
                    else:
                        path.pop()
                        state.set_state(next_state, next_maps)
                    break
            except:
                return None

def heuristic(state, goal,heur='none'):
    if heur == 'none':
        return 0
    if heur == 'l1':
        return sum([abs(x-y) for x,y in zip(state,goal)])//2
                

def astar(state: Control):
    stack = [[0, [state.start]], ]
    heap = [[0, state.start], ]
    costs = {tuple(tuple(x) for x in state.start) : (0, None)}
    while heap:
        current_cost, current_state = heappop(heap)
        _, current_maps = state.stack.pop()
        state.visted.append((current_state, current_maps))
        print([x.__name__ for x in state.moves])
        for move in state.moves:
            state.set_state(current_state, current_maps)
            if move():
                print(move.__name__,current_state,current_cost,len(heap),heuristic(state.current[0],state.end[0],heur='l1'))
                if state.check_goal():
                    costs[tuple(tuple(x) for x in state.current)] = (current_cost + 1, current_state)
                    path = []
                    print(state.current)
                    cur = state.current
                    while cur:
                        path.append(cur)
                        cur = costs[tuple(tuple(x) for x in cur)][1]
                    path.reverse()
                    print(path)
                    return path
                if tuple(tuple(x) for x in state.current) not in costs:
                    print('new',state.current)
                    costs[tuple(tuple(x) for x in state.current)] = (current_cost + 1, current_state)
                    heappush(heap, [current_cost + 1 + heuristic(state.current[0],state.end[0],'none'), state.current])
                elif current_cost + 1 < costs[tuple(tuple(x) for x in state.current)][0]:
                    print('update')
                    costs[tuple(tuple(x) for x in state.current)] = (current_cost + 1,current_state)
            print('cant',)
    #print('shiT!','\n'.join([str(x)+': '+str(y)+'\n' for x,y in costs.items()]),heap)
    return None, step
#[[[3, 1]], [[3, 2], [3, 3]], [[4, 2], [4, 3]], [[4, 4]], [[4, 5], [4, 6]], [[4, 7]], [[3, 7], [2, 7]], [[3, 8], [2, 8]], [[4, 8]],
# [[4, 9], [4, 10]], [[4, 11]], [[4, 12], [4, 13]], [[4, 14]], [[3, 14], [2, 14]], [[3, 13], [2, 13]], [[1, 13]]]
                    

# def astar(self,start,goal,env,rod,dist='A'):
#     Q = []
#     C = {}
#     C_space = self.C_space(env,rod)
#     heappush(Q,(0,start))
#     C[start] = 0
#     parent_table = {start:None}
#     step=0
#     while Q:
#         step+=1
#         now = heappop(Q)
#         if now[1] == goal:
#             print('Number of steps: {}\nFinal cost: {}'.format(step,C[goal]))
#             return(self.plan(goal,parent_table))
#         for neighbor in self.neighbors(now[1],C_space):
#             if neighbor not in parent_table:
#                 parent_table[neighbor]= now[1]
#                 cost = C[now[1]]+1
#                 C[neighbor]=cost
#                 heappush(Q,(cost+self.distance(neighbor,goal,dist),neighbor))
#             else:
#                 if C[now[1]]+1<C[neighbor]:
#                     C[neighbor] = C[now[1]]+1
#                     parent_table[neighbor] = now


            
def handle(state: Control, map_size= (0,0)):
    state.Play_handle = True
    pygame.init()
    display = Display(title='Bloxorz Game', map_size=map_size)
    result = True
    print("Press Space Key to Exit!")
    while True:
        # os.system("clear")
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
                
            if display.quit(event):
                return
        state.draw_maps()
        state.draw_box()
        # state.print_maps()
        display.update()

        if state.check_goal():
            print("WINNER!")
            return
        if result == False:
            print("LOSER!")
            return