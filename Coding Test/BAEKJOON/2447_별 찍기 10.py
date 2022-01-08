# 2447, 별 찍기 10 | others
import time

start = time.time()
# print('time', time.time() - start)

import sys
import copy

sinput = sys.stdin.readline
sprint = sys.stdout.write

N = int(input())

stars_board = ['*' for _ in range(N)]
star_board = '*'

x = 1
while x != N:
    for i in range(3):
        board = [' '*x for _ in range(x)] if i == 1 else star_board
        for j in range(x):
            stars_board[x*i+j] = star_board[j] + board[j] + star_board[j]
    x *= 3
    star_board = copy.deepcopy(stars_board[:x])

sprint('\n'.join(stars_board))


# 간단, 오래걸림
'''
for i in range(N):
    for j in range(N):
        count = N // 3
        while count >= 1:
            if i // count % 3 == 1 and j // count % 3 == 1:
                sprint(' ')
                break
            count //= 3
        else:
            sprint('*')
    sprint('\n')
'''

print('time', time.time() - start)


