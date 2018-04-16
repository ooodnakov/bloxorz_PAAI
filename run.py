#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run"""
from model.map import maps
from model.sw import swO, swQ, swX
from model.bridge import Bridge
from model.solver import *

if __name__=="__main__":
    level =  maps("./level/demo2.json")
    level.print_current()
    dfs(Control(level))


