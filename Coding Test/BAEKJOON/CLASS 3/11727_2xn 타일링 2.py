# 11727th, 2×n 타일링 2 | class 3

import time

start = time.time()
# print('time', time.time() - start)

import sys
import math
from functools import reduce 

sinput = sys.stdin.readline
sprint = sys.stdout.write

n = int(sinput())

# DP
'''
dp_table = [0, 1, 3]
for i in range(3, n+1):
    dp_table.append(dp_table[i-1] + 2*dp_table[i-2])
answer = dp_table[n]
sprint(str(answer % 10007)+'\n')
'''

# combination with repetition

answer = 0
for wider_num in range(n//2 + 1):
    taller_num = n - 2 * wider_num
    answer += math.comb(wider_num+taller_num, taller_num)*pow(2,wider_num)
    
sprint(str(answer % 10007)+'\n')
