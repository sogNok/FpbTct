# 9095th, 1,2,3 더하기 | class 3

import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

dp_table = [0] * 12
dp_table[1] = 1
dp_table[2] = 2
dp_table[3] = 4

def num_of_way(n):
    global dp_table
    if dp_table[n]:
        return dp_table[n]
    
    with3 = dp_table[n-3] if dp_table[n-3] else num_of_way(n-3) 
    with2 = dp_table[n-2] if dp_table[n-2] else num_of_way(n-2)    
    with1 = dp_table[n-1] if dp_table[n-1] else num_of_way(n-1)

    dp_table[n] = with1 + with2 + with3
    return dp_table[n]

def num_of_way2(n):
    global dp_table
    if dp_table[n]:
        return dp_table[n]
    
    for i in range(4,n+1):
        dp_table[i] = dp_table[i-1] + dp_table[i-2] + dp_table[i-3]
    return dp_table[n]
    
num_of_way2(10)
T = int(sinput())

for _ in range(T):
    n = int(sinput())
    sprint(str(num_of_way2(n))+'\n')
