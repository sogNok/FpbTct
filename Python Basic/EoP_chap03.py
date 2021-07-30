# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 14:48:02 2021

@author: 이충섭
"""

# Chapter 03 organization

a = int(input('Integer a: '))
b = int(input('Integer b: '))
c = int(input('Integer c: '))
d = int(input('Integer d: '))

if      a: print('a is not zero.')  # If not 0 then Ture
if not  b: print('b is zero.')      # If not 0 then False

# Place the first nonzero value of a, b, and c into x, 
# and if all are zero, place d int x
x = a or b or c or d
print('x = ', x)

if d % c:                           # The modulo of d divided by c is not zero
    print('c is not divisor of d.')
else:
    print('c is divisor of d.')
    
print('c is' + ('odd number' if c % 2 else 'even number') + '.')

print('Evaluation of score d: ', end='')
if d < 0 or d > 100:                # Other than 0 ~ 100
    print('Incorrect score')
elif d >= 60:
    print('Pass')                   # 60 ~ 100
else:
    print('Non-pass')                 # 0 ~ 59