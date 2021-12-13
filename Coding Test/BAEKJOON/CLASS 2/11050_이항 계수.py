# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 18:38:29 2021

@author: 이충섭
"""

# 11050th, 이항 계수 1 | class 2

N, K = map(int, input().split())

if K >= N//2 + 1: K = N-K

if K == 0:
    print(1)
else:
    n, k = 1,1
    for i in range(0, K):
        n *= N-i
        k *= K-i
    else:
        print(n//k)
        
#%%
# 참조 닶
# 특이함
def combine(n, k):
    if k == 0:
        return 1
    if k == n:
        return 1
    if memo[n][k] != -1:
        return memo[n][k]
    return combine(n - 1, k - 1) + combine(n - 1, k)


N, K = [int(x) for x in input().split(' ')]
memo = [[-1 for k in range(K + 1)] for n in range(N+1)]
print(memo[-1][1])
print(combine(N, K))