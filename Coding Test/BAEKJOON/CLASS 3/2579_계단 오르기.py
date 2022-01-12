# 2579th, 계단 오르기 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

input_list = sys.stdin.read().splitlines()

N = int(input_list[0])
stair_scores = input_list[1:].reverse()
sum_score = int(stair_scores[0])
is_Second = True
is_Third = False

for itr in range(1, N):
    if is_Third: is_Third = False; continue
    
    
print('time', time.time() - start)


