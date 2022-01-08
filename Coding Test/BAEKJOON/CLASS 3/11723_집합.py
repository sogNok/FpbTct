# 11723rd, 집합 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

S = list(False for _ in range(20))
for _ in range(int(sinput())):
    opr = sinput().split()

    if opr[0] == 'add':
        S[int(opr[1]) - 1] = True
    elif opr[0] == 'remove':
        S[int(opr[1]) - 1] = False
    elif opr[0] == 'check':
        if S[int(opr[1]) - 1]:  sprint('1\n')
        else:                   sprint('0\n')
    elif opr[0] == 'toggle':
        if S[int(opr[1]) - 1]:  S[int(opr[1]) - 1] = False
        else:                   S[int(opr[1]) - 1] = True
    elif opr[0] == 'all':
        S = list(True for _ in range(20))
    else:
        S = list(False for _ in range(20))

print('time', time.time() - start)


