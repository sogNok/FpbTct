# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 21:02:27 2021

@author: 이충섭
"""

# Chapter 12 organization 1

class RangeException(Exception):
    """ Exception out of range """
    pass
    
class ParameterRangeException(RangeException):
    """ Exception out of range of parameters """
    pass

class ResultException(RangeException):
    """ Exception out of range of return values """
    pass

def is_valid(value: int) -> bool:
    """ Is the value 0~9? """
    return 0 <= value <= 9

def add(a: int, b: int) -> int:
    """ Return the sum of a and b
    
    Precondition : a and b are 0~9
            Send ParameterRangeException if not met  
    
    Postcondition : Return sum is 0~9
            Send ResultException if not met 
            
    """
    if not is_valid(a):
        raise ParameterRangeException
    if not is_valid(b):
        raise ParameterRangeException
        
    result = a + b
    
    if not is_valid(result):
        raise ResultException
    return result

a = int(input('Integer a : '))
b = int(input('Integer b : '))

try:
    print(f'The sum of the two numbers is {add(a, b)}.')
except RangeException:
    print('Out of range.')
except:
    print('Exception has occurred.')
finally:
    print('It`s done.')