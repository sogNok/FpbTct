# 1764th, 듣보잡 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys
import bisect

sinput = sys.stdin.readline
sprint = sys.stdout.write


N, M = map(int, sinput().split())

D = set(sinput().rstrip() for _ in range(N))
DBJ = []
for _ in range(M):
    B = sinput().rstrip()
    if B in D: DBJ.insert(bisect.bisect_left(DBJ, B), B)

DBJ.insert(0, str(len(DBJ)))
sprint('\n'.join(DBJ))

# 참조 답
# set의 성질 이용
'''
import sys
n, m = map(int, input().split())
nameList = sys.stdin.read().splitlines()
hearset = set(nameList[:n])
seeset = set(nameList[n:])
ret = list(hearset & seeset)
ret.sort()
print(len(ret))
for i in ret:
    print(i)
'''
print('time', time.time() - start)


