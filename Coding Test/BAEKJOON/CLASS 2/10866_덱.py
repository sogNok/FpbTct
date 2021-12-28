# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 15:36:04 2021

@author: 이충섭
"""

# 10866th, 덱 | class 2

from sys import stdin

def deque_func(stack: list, opr: str):
    if 'push_front' in opr:
        operation, num = opr.split()
        stack.insert(0, num)
    elif 'push_back' in opr:
        operation, num = opr.split()
        stack.append(num)
    elif opr == 'pop_front':
        if not stack:   print('-1')
        else:           print(stack.pop(0))
    elif opr == 'pop_back':
        if not stack:   print('-1')
        else:           print(stack.pop())
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
deque = []

for line in stdin:
    opr = line.rstrip()
    deque_func(deque, opr)