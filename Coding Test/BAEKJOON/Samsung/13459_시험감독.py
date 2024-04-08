# 13458th, 시험감독 | Samsung

import time

start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write


N = int(sinput())
A_list = list(map(int, sinput().split()))
B, C = map(int, sinput().split())
count = 0

for i in range(N):
    count += 1
    remain = A_list[i] - B
    
    if remain > 0:
        quotinent, remainder = divmod(remain, C)
        count += quotinent
        if remainder:
            count += 1
            
print(count)

