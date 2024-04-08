# 14501st, 퇴사 | Samsung

import time

start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write


N = int(sinput())

dp_table = [0] * N
consulting = []

for i in range(N):
    T, P = map(int, sinput().split())
    consulting.append(T)
    max_earn = 0
    
    for j in range(i):
        if i-j >= consulting[j]:
            max_earn = max(max_earn, dp_table[j])
    
    P = 0 if N-i < T else P
    dp_table[i] = max_earn + P

print(max(dp_table))

# 참조답 O(n)
'''
n = int(input())
T = []
P = []
for i in range(n):
    Ti, Pi = map(int, input().split())

    if i + Ti > n:
        Ti = 0
        Pi = 0

    T.append(Ti)
    P.append(Pi)

dp = [0]*16

for i in range(n-1, -1, -1):
    dp[i] = max(dp[i+1], dp[i+T[i]] + P[i])

print(dp[0])
'''
