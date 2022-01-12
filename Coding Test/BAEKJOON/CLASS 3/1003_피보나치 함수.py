# 1003rd, 피보나치 함수 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

for _ in range(int(sinput())):
    N = int(sinput())
    a,b = (0, 1) if N else (1, 0)
    for _ in range(N-1):
        a, b = b, a+b
    sprint(f'{a} {b}\n')


print('time', time.time() - start)


# 참조 답
# DP 사용 전 구간 탐색 및 저장 해두기
'''
from sys import stdin
T = int(input())
l = [int(stdin.readline()) for _ in range(T)]
f = [[1, 0], [0, 1]]
for i in range(2, max(l)+1):
    f.append([f[i-2][0]+f[i-1][0], f[i-2][1]+f[i-1][1]])

for i in l:
    print(' '.join(map(str, f[i])))
'''