# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 14:54:58 2021

@author: 이충섭
"""

# 10828th, 스택 | class 2

import sys

def stack_func(stack: list, opr: str):
    if 'push' in opr:
        operation, num = opr.split()
        stack.append(num)
    elif opr == 'pop':
        if not stack:   print('-1')
        else:           print(stack.pop())
    elif opr == 'size': print(len(stack))
    elif opr == 'empty':
        if not stack:   print('1')
        else:           print('0')
    else:
        if not stack:   print('-1')
        else:           print(stack[-1])
        
N = int(sys.stdin())
stack = []

for _ in range(N):
    opr = sys.stdin.readline()
    stack_func(stack, opr)
    
#%%
# 참조 답1
# stdin만 쓰기
from sys import stdin

stack = []
next(stdin)
for line in stdin:
    command = line.split()
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if stack: print(stack.pop())
        else: print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if stack: print(0)
        else: print(1)
    elif command[0] == 'top':
        if stack: print(stack[-1])
        else: print(-1)
        
#%%
# 참조 답2
# dictionary 쓰기

import sys

stack = list()

command = dict(
    push=lambda x: stack.append(x),
    pop=lambda: stack.pop() if stack else -1,
    size=lambda: len(stack),
    empty=lambda: 0 if stack else 1,
    top=lambda: stack[-1] if stack else -1
    )

in_data = sys.stdin.readlines()
for c in in_data[1:]:
    c = c.strip()
    if c[:2] == 'pu':
        command['push'](c.split()[1])
    else:
        print(command[c]())