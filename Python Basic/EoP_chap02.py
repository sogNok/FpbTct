# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 10:54:37 2021

@author: 이충섭
"""
# Chapter 02 organization

print('ABC', 'XYZ')
print('ABC', 'XYZ', end='')     # Do not change the line at the end of row
print('ABC', 'XYZ', sep='')     # Do not include spaces for seperation
print()                         # Change the line
print('ABC\n\nXYZ', sep='')     # Change the line twice in the middle
print()                         # Change the line

s = input('String: ')
print('You', 'entered', s, '.')
print('You' + 'entered' + s + '.')
print('You entered {}.'.format(s))
print(f'You entered {s}.')
print()

no = int(input('Integer value: '))
print('Value of last digit : ', str(no % 10), sep='')
print('Binary: ' + bin(no))             # Convert to Binary String
print('Octal: ' + oct(no))              # Convert to Octal String
print('Decimal: ' + str(no))            # Convert to Decimal String
print('Hex: ' + hex(no))                # Convert to Hex String
print()

PI = 3.14159                            # Number representing PI
print('Find the area of the square and the circle')
width = float(input('Horizontal length of a square : '))
height = float(input('Vertival length of a square : '))
radius = float(input('Radius of a circle : '))

print(f'Square: {width * height}')
print(f'Circle: {PI * radius * radius}')