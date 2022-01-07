# 18111th, 마인크래프트 | class 2
import time
start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

N, M, B = map(int, input().split())
blocks = []
for _ in range(N):
    blocks.extend(map(int, input().split()))

min_time, last_height = sys.maxsize, 0
h = max(blocks)

for height in range(h + 1):
    time_limit = 0
    block_num = B
    
    for block in blocks:
        diff = block - height
        block_num += diff
        if diff > 0:
            time_limit += 2 * diff
        else:
            time_limit -= diff
    
    if block_num < 0:
        pass
    elif time_limit <= min_time:
        min_time = time_limit
        last_height = height
        
print(min_time, last_height)

print('time', time.time() - start)


    