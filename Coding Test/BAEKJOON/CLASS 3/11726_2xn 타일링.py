# 11726th, 2×n 타일링 | class 3

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

dp_table = [0, 1, 2]
for i in range(3, n+1):
    dp_table.append(dp_table[i-1] + dp_table[i-2])
answer = dp_table[n]
sprint(str(answer % 10007)+'\n')


# combination with repetition
'''
answer = 0
for wider_num in range(n//2 + 1):
    taller_num = n - 2 * wider_num
    #answer += math.comb(wider_num+taller_num, taller_num)
    
    l = taller_num if taller_num > wider_num else wider_num
    s = taller_num + wider_num - l
    
    numerator = reduce(lambda x,y: x*y, range(l+1, l+s+1)) if s else 1
    denominator = reduce(lambda x,y: x*y, range(1, s+1)) if s else 1
    answer += numerator // denominator

sprint(str(answer % 10007)+'\n')
'''
