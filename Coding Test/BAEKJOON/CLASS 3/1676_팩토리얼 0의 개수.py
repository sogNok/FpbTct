# 1676th, 팩토리얼 0의 개수 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

N = int(input())
print(N//5 + N//25 + N//125)


print('time', time.time() - start)


