# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:42:45 2021

@author: 이충섭
"""

size = int(input('size: '))
dalpaeng = [[0 for _ in range(size)] for _ in range(size)]

start = 0
end = size
row = 0
column = size
idx = 1

while True:
    # Top
    for i in range(start, end):
        dalpaeng[start][i] = idx
        idx += 1
    start += 1
    if idx > size**2:
        break
    # Right
    for i in range(start, end):
        dalpaeng[i][end-1] = idx
        idx += 1
    if idx > size**2:
        break
    # Bottom
    for i in range(start, end):
        dalpaeng[end-1][size-i-1] = idx
        idx += 1
    end -= 1
    if idx > size**2:
        break
    # left
    for i in range(start, end):
        dalpaeng[size-1-i][start-1] = idx
        idx += 1
    if idx > size**2:
        break


print('-'*27)
for i in range(size):
    for j in range(size):
        print(f'{dalpaeng[i][j]:4d}', end='')
    print()
print('-'*27)