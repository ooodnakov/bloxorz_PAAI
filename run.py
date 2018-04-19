#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Run"""
from model.map import maps
from model.sw import swO, swQ, swX
from model.bridge import Bridge
from model.solver import *
if __name__=="__main__":
    level =  maps("./level/demo4.json")
    # handle(Control(level))
    # bfs_step_by_step(Control(level), timesleep=0.5)
    dfs_step_by_step(Control(level), timesleep=0.5)
    # bfs(Control(level))
    # dfs_path(Control(level))
    # bfs_path(Control(level))
    # dfs_recursion(Control(level))


