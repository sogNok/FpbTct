# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 16:32:59 2021

@author: 이충섭
"""

# Chapter 10 organization

import EoP_chap10_sub

print('Left side Perpendicular Isoseceles Triangle')
n = int(input('Length of short side: '))

# Output '*' a PIT with short side lenght n
for i in range(1, n+1):
    EoP_chap10_sub.put_star(i)
    print()
    
print('Rectangle')
h = int(input('Height: '))
w = int(input('Width: '))

# Draw rectangle with h height and w width as '+'
for _ in range(1, h+1):
    EoP_chap10_sub.puts(n=w, s='+')
    print()
    
# Output a documentation string for module EoP_chap10_sub
print('\n' + EoP_chap10_sub.__doc__)