# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:30:41 2021

@author: 이충섭
"""

# 1920th, 수 찾기 | class 2

import sys

sys.stdin.readline()

A = sorted(map(int, sys.stdin.readline().split()))

sys.stdin.readline()

M = list(map(int, sys.stdin.readline().split()))

for x in M:
    l = 0
    r = len(A) - 1
    m = 0
    
    while r > l:
        m = (r+l) // 2
        
        if x > A[m]:
            l = m + 1
        elif x < A[m]:
            r = m - 1
        else:
            l = m
            break

    sys.stdout.write('1\n' if x == A[l] else '0\n')
    
#%%
# 참조 
ip = input
def main():
    ip()
    n = ip().strip().split(' ')
    ip()
    
    s = set(n)
    r = ''
    for k in input().strip().split(' '):
        r += '1\n' if k in s else '0\n'
    print(r)

if __name__ == "__main__":
    main()