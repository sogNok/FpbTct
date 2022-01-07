# 2805th, 나무 자르기 | class 2
import time
start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

N, M = map(int, sinput().split())
tree_list = list(map(int, sinput().split()))


h = sum(tree_list) // N
N = M // N + 1
l, r = h - N, max(tree_list)
sum_tree = 0

while l <= r:
    sum_tree = 0
    h = (l + r) // 2
    
    for height in tree_list:
        if height > h:
            sum_tree += height - h
    
    if sum_tree >= M:
        l = h+1
    else:
        r = h-1


print(r)
        

print('time', time.time() - start)

# 참조 답
# counter 이용
'''
import sys
from collections import Counter
n, m = map(int, sys.stdin.readline().split())
s = Counter(map(int, sys.stdin.readline().split()))

l = 1
r = max(s)

while l <= r:
    mid = (l + r) // 2
    x = sum((i-mid)*j for i, j in s.items() if i > mid)

    if x >= m:
        l = mid + 1
    else:
        r = mid - 1

print(r)
'''

    