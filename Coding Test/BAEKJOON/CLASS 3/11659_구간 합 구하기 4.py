# 11659th, 구간 합 구하기 4 | class 3

import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

N, M = map(int, sinput().split())
num_list = list(map(int, sinput().split()))
acc_list = [0]
answer = []
for i in range(N):
    acc_list.append(acc_list[i] + num_list[i])

for _ in range(M):
    i, j = map(int, sinput().split())
    answer.append(str(acc_list[j] - acc_list[i-1]))

sprint('\n'.join(answer))
