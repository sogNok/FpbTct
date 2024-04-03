# 27866th, 문자와 문자열 | class 1

import time

start = time.time()
# print('time', time.time() - start)

import sys

sread = sys.stdin.readline
swrite = sys.stdout.write

S = sread().rstrip()
N = int(sread())

swrite(S[N-1])
