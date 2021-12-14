# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 12:52:58 2021

@author: 이충섭
"""

# 2609th, 최대공약수와 최소공배수 | class 2
import sys # int(sys.stdin.readline().r l strip())

A, B = map(int, input().split())

GCD = 0
LCM = 0

for x in range(1, min(A, B)+1):
    if A % x == 0 and B % x == 0:
        GCD = max(GCD, x)
    
LCM = A * B // GCD

print(GCD)
print(LCM)

#%%
# 참조 답
# using Euclidean algorithm

def gcd(x, y):
    if y != 0:
        return gcd(y, x%y)
    else :
        return x

A, B = map(int, input().split())

GCD = gcd(A, B)
LCM = A * B // GCD
print(GCD)
print(LCM)