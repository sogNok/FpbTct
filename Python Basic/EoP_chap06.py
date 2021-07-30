# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:43:59 2021

@author: 이충섭
"""

# Chapter 06 organization

s1 = input('String s1: ')
s2 = input('String s2: ')

idx = s1.find(s2)
if idx == -1:
    print('s1 does not contain s2')
else:
    print(s1)
    # Output s2 after idx spaces
    print(' ' * idx, end='')
    print(s2)
    
    # Reverse all s2 contained in s1
    s1 = s1.replace(s2, s2[::-1])
    print()
    print('That part has been reversed')
    print(s1)
    
    # Remove all s2[::-1] contained in s1
    s1 = s1.replace(s2[::-1], '')
    print()
    print('That part has been removed')
    print(s1)
print()

# Use of the format method
x = float(input('Real Value: '))
w = int(input('Total Digits: '))
p = int(input('Mantissa Digits: '))

print('{{:{}.{}f}}'.format(w, p).format(x))
