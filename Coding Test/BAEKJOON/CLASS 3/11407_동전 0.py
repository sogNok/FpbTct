# 11407th, 동전 0 | class 3

import time

start = time.time()
# print('time', time.time() - start)

import sys
from bisect import bisect_left

sinput = sys.stdin.readline
sprint = sys.stdout.write

N, K = map(int, sinput().split())
coin_list = [int(sinput()) for _ in range(N)]
coin_count = 0

# if N is larger
'''
while K != 0:
    index = bisect_left(coin_list, K)

    if index != len(coin_list):
        if K == coin_list[index]:
            coin_count += 1
            break
    
    quotient, remainder = divmod(K, coin_list[index-1])
    coin_count += quotient
    K = remainder
    coin_list = coin_list[:index-1]
'''

for i in range(N-1, -1, -1):
    if coin_list[i] > K:
        continue
    else:
        quotient, remainder = divmod(K, coin_list[i])
        coin_count += quotient
        K = remainder
        
sprint(str(coin_count))
