#!usr/bin/env python3
'''
Simple example of decorators with arguments.
Having *args, **kwargs in the wrapper let's the wrapper function
to pass arguments to the function.
'''

def my_decorator(fun):
    def wrapper(*args,**kwargs):
        print('Do something before func call')
        fun(*args,**kwargs)
        print('Do something after func call')
    return wrapper

@my_decorator
def hello(name):
    print(f'Hello {name}!')

@my_decorator
def hello2(name1,name2):
    print(f'Hello {name1} and {name2}!')

#hello()
hello('Groooot')
print('\n')
hello2('Groooot','Drax')


