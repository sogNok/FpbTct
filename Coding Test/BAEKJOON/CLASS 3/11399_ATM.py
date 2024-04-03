# 11399th, ATM | class 3

import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

N = int(sinput())
awaiters = sorted(map(int, sinput().split()))
waiting_time = 0

for i in range(N):
    waiting_time += awaiters.pop() * (i+1)
    
sprint(str(waiting_time))
