# 1003rd, 피보나치 함수 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

N, M = map(int, sinput().split())
input_list = sys.stdin.read().splitlines()

sites = dict(inputs.rstrip().split() for inputs in input_list[:N])
questions = input_list[N:]

# 다른 방식 더느림
'''
sites = dict(sinput().rstrip().split() for _ in range(N))
questions = [sinput().rstrip() for _ in range(M)]
'''
sprint('\n'.join(sites.get(quest) for quest in questions))

print('time', time.time() - start)


