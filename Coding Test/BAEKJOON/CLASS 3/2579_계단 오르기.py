# 2579th, 계단 오르기 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

input_list = sys.stdin.read().splitlines()

N = int(input_list[0])
stair_scores = list(map(int, reversed(input_list[1:])))

if N == 1:
    print(stair_scores[0])
    sys.exit(0)

sum_score = [stair_scores[0], stair_scores[0], stair_scores[0]+stair_scores[1]]

for itr in range(2, N):
    first, second, third = sum_score

    sum_score[0] = second if second > third else third
    sum_score[1] = first + stair_scores[itr]
    sum_score[2] = second + stair_scores[itr]

print(max(sum_score))

# 참조 답
# 같은 알고리즘
# 더 빠름
'''
from sys import stdin

a,b,c = 0,0,0

n = int(stdin.readline())
for _ in range(n):
    pb = int(stdin.readline())
    d_0,d_1,d_2 = max(b,c),a+pb,b+pb
    a,b,c = d_0,d_1,d_2

print(max(d_2,d_1))
'''