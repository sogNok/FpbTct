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


