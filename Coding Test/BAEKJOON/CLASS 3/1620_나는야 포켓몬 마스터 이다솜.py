# 1620th, 나는야 포켓몬 마스터 이다솜 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

M, N = map(int, sinput().split())
poketmons = [sinput().rstrip() for _ in range(M)]
hash_poketmons = {poketmon:i+1 for i,poketmon in enumerate(poketmons)}

for _ in range(N):
    question = sinput().rstrip()
    if ord(question[0]) >= 65:
        sprint(str(hash_poketmons.get(question)))
    else:
        sprint(poketmons[int(question)-1])
    sprint('\n')

print('time', time.time() - start)


