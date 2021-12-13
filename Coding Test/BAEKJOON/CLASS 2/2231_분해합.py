# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:31:05 2021

@author: 이충섭
"""

# 2231st, 분해합 | class 2

N = int(input())

M = 0

for x in range(N):
    M = x
    for digit in str(x):
        M += int(digit)
    
    if M == N:
        print(x)
        break
else:
    print(0)
    
#%%
# 더 빠르게

N = int(input())


M = N - len(str(N)) * 9

if M < 0:
    M = 0


for x in range(M, N):
    M = x
    for digit in str(x):
        M += int(digit)
    
    if M == N:
        print(x)
        break
else:
    print(0)
    
#%%
# 참조

N=int(input())
r=0
for i in range(max(0, N-100), N):
 if sum(map(int,list(str(i))))+i==N:r=i;break
print(r)