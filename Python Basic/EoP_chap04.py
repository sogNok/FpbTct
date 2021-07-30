# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:17:30 2021

@author: 이충섭
"""

# Chapter 04 organization

while True:
    n = int(input('Integer between 0~100: '))
    if 0 <= n <= 100:
        break
    
c = n

# Output '*' c times
while n > 0:
    print('*', end='')
    n -= 1
print()

# Output 1,2,3,4,5,6,7,8,9,0 repeatedly c times
for i in range(1, c+1):
    print(i % 10, end='')
print('\n')

# Outputs height and width integers when area is s
s = int(input('area: '))
print(f'area is {s}, height and width integers:')
for i in range(1, s+1):
    if i**2 > s: break
    if s % i: continue
    print(f'{i}x{s//i}')
print()

# Output n '*' every w-th time
n = int(input('How many * do you print: '))
w = int(input('How many times do you refresh a new line: '))
for i in range(1, n + 1):
    print('*', end='')
    if i % w == 0:
        print()
if n % w:
    print()
print()

# Draw a rectangle with numbers
h = int(input('height: '))
w = int(input('width: '))
for i in range(1, h+1):
    for j in range(1, w+1):
        print((i + j - 1) % 10, end='')
    print()
