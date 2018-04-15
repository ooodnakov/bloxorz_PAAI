#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Run"""
from model.map import maps
from model.sw import swO, swQ, swX
from model.bridge import Bridge

def logic(map):
    pass

if __name__=="__main__":
    test =  maps("./level/demo.json")
    test.print_current()
    # obj = swX("x1", 0, True, [3, 4], Bridge("c1", True, [[3,6],[3,7]]))
    # test.updateSWX(obj)
    # test.print_current()
