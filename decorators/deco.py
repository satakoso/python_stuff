#!usr/bin/env python3
'''
Simple example of decorators
-- 
After: moi = my_decorater(hello)
moi is wrapped function. moi is a 'wrapper'.
and moi() is function call that executes this wrapper function.

'''

def my_decorater(func):
    def wrapper():
        print('First do something')
        func()
        print('After func() call, do something else')
    return wrapper

def hello():
    print('Hello')

moi = my_decorater(hello)
print('>>hello():')
hello()
print('>>moi():')
moi()
print('>>moi')
print(moi)
