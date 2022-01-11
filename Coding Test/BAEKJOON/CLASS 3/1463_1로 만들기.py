# 1003rd, 피보나치 함수 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

def reduct_to_one(n:int):
    if n == 1: return 0
    A, B, C, D, E = 0, 0, 1, sys.maxsize, sys.maxsize
    while C <= n:
        C *= 3
        A += 1
    A = n-C//3 + A-1
    C = 1
    while C <= n:
        C *= 2
        B += 1
    B = n-C//2 + B-1
    C = sys.maxsize
    if not n % 3:
        C = reduct_to_one(n//3) + 1
    if not n % 2:
        D = reduct_to_one(n//2) + 1

    E = reduct_to_one(n-1) + 1

    return min(A,B,C, D, E)

N = int(input())

print(reduct_to_one(N))

print('time', time.time() - start)


