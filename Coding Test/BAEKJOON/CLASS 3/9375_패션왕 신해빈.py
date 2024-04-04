# 9375th, 패션왕 신해빈 | class 3

import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

T = int(sinput())

for _ in range(T):
    n = int(sinput())
    cloth_dict = dict()
    answer = 1
    
    for _ in range(n):
        value, key = sinput().split()
        if key in cloth_dict:
            cloth_dict[key] += 1
        else:
            cloth_dict[key] = 1
    
    cloth_list = list(cloth_dict.values())
    
    for val in cloth_list:
        answer *= val + 1
    
    sprint(str(answer-1)+'\n')
