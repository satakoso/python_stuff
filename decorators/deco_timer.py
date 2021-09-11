#!usr/bin/env python3
'''
Simple example of using wrapper as a counter on function
execution time.
Btw. numpy is faster, of course.
'''

from time import perf_counter
import numpy as np

def my_decorator(func):
    def wrapper():
        Ti = perf_counter()
        func()
        Tf = perf_counter()
        print(f'It took {Tf -Ti} secons to run the function')
    return wrapper

@my_decorator
def array_squared():
    x = np.arange(0,100000,1)
    x = x**2

@my_decorator
def list_squared():
    y = [x**2 for x in range(0,100000)]

array_squared()
list_squared()

