# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 11:46:09 2021

@author: 이충섭
"""

# Chapter 05 organization

a, b = 5, 7
c = b
print('a, b, c = {}, {}, {}'.format(a, b, c))
print('id(5) = {}'.format(id(5)))
print('id(7) = {}'.format(id(7)))
print('id(a) = {}'.format(id(a)))
print('id(b) = {}'.format(id(b)))
print('id(c) = {}'.format(id(c)))

a, b = b, a
c += 1

print('swap a and b, increase c by 1')
print('a, b, c = {}, {}, {}'.format(a, b, c))
print('id(5) = {}'.format(id(5)))
print('id(7) = {}'.format(id(7)))
print('id(8) = {}'.format(id(8)))
print('id(a) = {}'.format(id(a)))
print('id(b) = {}'.format(id(b)))
print('id(c) = {}'.format(id(c)))
print('a is 5 = {}'.format(a is 5))
print('a is 7 = {}'.format(a is 7))
print('a is 8 = {}'.format(a is 8))