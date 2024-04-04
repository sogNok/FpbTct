# 9461st, 파도반 수열 | class 3

import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

T = int(sinput())
P = [0] * 101
P[1] = 1
P[2] = 1
P[3] = 1
P[4] = 2
P[5] = 2

for _ in range(T):
    N = int(sinput())
    
    for i in range(6, N+1):
        P[i] = P[i-1] + P[i-5]
    
    sprint(str(P[N])+'\n')
