# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 15:29:12 2021

@author: 이충섭
"""

# 10845th, 큐 | class 2

from sys import stdin

def queue_func(stack: list, opr: str):
    if 'push' in opr:
        operation, num = opr.split()
        stack.append(num)
    elif opr == 'pop':
        if not stack:   print('-1')
        else:           print(stack.pop(0))
    elif opr == 'size': print(len(stack))
    elif opr == 'empty':
        if not stack:   print('1')
        else:           print('0')
    elif opr == 'front':
        if not stack:   print('-1')
        else:           print(stack[0])
    else:
        if not stack:   print('-1')
        else:           print(stack[-1])
        
next(stdin)
queue = []

for line in stdin:
    opr = line.rstrip()
    queue_func(queue, opr)