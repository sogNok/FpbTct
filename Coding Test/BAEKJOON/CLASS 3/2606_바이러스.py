# 2606th, 바이러스 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

N = int(input())
T = int(input())
input_list = [map(int, sinput().split()) for _ in range(T)]

infected_list = [N+1] * (N+1)
infected_list[0] = 0
infected_list[1] = 0


for inputs in input_list:
    a, b = inputs
    if infected_list[a] == 0: infected_list[b] = 0
    elif infected_list[b] == 0: infected_list[a] = 0
    else:
        infected_list[a] = b
        infected_list[b] = a

count = 0
for is_true in infected_list:
    if is_true:
        count += 1

print(count)

print('time', time.time() - start)