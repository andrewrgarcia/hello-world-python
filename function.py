import numpy as np
import matplotlib.pyplot as plt

'functions are created by the def call (definition) followed by a space and \
the name of the function. This first function is called "function1" '
def function1():
    print('function 1: my first function')

'to execute your function, must call it as it is done below:'
function1()


def function2(x,y):
    result = x+y
    
    return result

'''this second function RETURNS a value with 2 inputs (x and y), \
value is not printed so it will not appear

the output of function2 can be defined as a variable'''
f2 = function2(3,4)

'then it can be printed'
print('function #2: ', f2)
      
'or operated with another number'
f2times2 = f2*2
print('function #2 x 2: ',f2times2)

'a function can also be put inside another function:'
print('a function within a function:')
inception = function2(function2(3,4),3)

print(inception)


