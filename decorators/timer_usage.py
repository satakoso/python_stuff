#!usr/bin/env python3
'''
Usage of deco_timer_module.py
'''

from deco_timer_module import timer

@timer
def squared_list():
    x = [x**2 for x in range(0,100000) ]


squared_list()
