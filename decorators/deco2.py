#!usr/bin/env python3
'''
using the @-sign before the function automatically wraps the 
function.
Essentially doing the: moi = my_decorator(moi)
and after that moi can be used as decorated function.
>>moi() 

'''
def my_decorator(func):
    def wrapper():
        print('First do something')
        func()
        print('After function call, do something else.')
    return(wrapper)

@my_decorator
def moi():
    print('Hello')

moi()

