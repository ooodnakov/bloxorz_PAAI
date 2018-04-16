#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run"""
from model.map import maps
from model.sw import swO, swQ, swX
from model.bridge import Bridge
from model.solver import *

if __name__=="__main__":
    level =  maps("./level/demo4.json")
    level.print_current()
    # handle(Control(level))
    # dfs(Control(level))
    print(dfs_path(Control(level)))
    # dfs_recursion(Control(level))


