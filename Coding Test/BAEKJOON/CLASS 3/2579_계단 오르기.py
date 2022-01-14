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
    if is_Second:
        
'''
10 20 30 40 50 60
11 00 11 11 00 11 140
11 11 00 00 11 11 140
11 00 11 00 11 11 150
11 11 00 11 11 00 
11 00 11 11 00 11

1 1
2 2
3 2
4 3
5 4
6 4
7 5
8 6
9 6
10 7

'''
    
print('time', time.time() - start)


