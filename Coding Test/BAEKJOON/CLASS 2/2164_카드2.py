# 2164th, 카드2 | class 2

import sys

N = int(sys.stdin.readline())

if N == 1: print(1); sys.exit(0)

power = 2
while power < N:
    power *= 2

if power == N: print(N)
else:
    power //= 2
    remain = N % power
    print(remain*2)

