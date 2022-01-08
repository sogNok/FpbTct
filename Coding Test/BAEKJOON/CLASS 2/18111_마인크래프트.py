# 18111th, 마인크래프트 | class 2
import time
start = time.time()
# print('time', time.time() - start)

import sys
from collections import Counter
sinput = sys.stdin.readline
sprint = sys.stdout.write

N, M, B = map(int, sinput().split())
blocks = []
for _ in range(N):
    blocks.extend(map(int, sinput().split()))

min_time, last_height = sys.maxsize, 0
sum_blocks = sum(blocks)

blocks = Counter(blocks)

min_height = min(blocks)
max_height = min(max(blocks), (sum_blocks + B) // (N*M))

for height in range(min_height, max_height + 1):
    time_limit = 0
    
    for block, num in blocks.items():
        diff = (block - height) * num
        if diff > 0:
            time_limit += 2 * diff
        else:
            time_limit -= diff
    
    if time_limit <= min_time:
        min_time = time_limit
        last_height = height
        
print(min_time, last_height)



print('time', time.time() - start)


    