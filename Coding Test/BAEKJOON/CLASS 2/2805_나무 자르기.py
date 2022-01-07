# 2805th, 소수 구하기 | class 2
import time
start = time.time()
print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

N, M = map(int, sinput().split())
tree_list = list(map(int, sinput().split()))
