#!usr/bin/env python3
'''
Simple module with timer decoration
'''
from time import perf_counter

def timer(func):
    def wrapper():
        Ti = perf_counter()
        func()
        Tf = perf_counter()
        print(f'It took function {func.__name__} {Tf -Ti} seconds to run the function')
    return wrapper
