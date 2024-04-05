# 17626th, Four Squares | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

def finding_squares(N:int, M:int):
    if M == 4:
        return 1
    argue = max(1, int(N**0.5))
    if N == argue ** 2:
        return 1

    min_count = sys.maxsize
    while N <= 3*argue**2:
        min_count = min(finding_squares(N-argue**2, M+1) + 1, min_count)
        argue -= 1
    return min_count

N = int(input())

print(finding_squares(N, 1))

# 참조 답
# 강력하고 간단한 답

'''
def p(n): print(n); exit()

n = int(input())

sq = {x * x for x in range(1, 224)}
if n in sq: p(1)

sq2 = {x + y for x in sq for y in sq if x + y <= 50000}
if n in sq2: p(2)

for x in sq:
	if n > x and n - x in sq2: p(3)

p(4)
'''

# DP pypy만 가능
'''
n = int(sinput())
dp_table = [5] * (n+1)

dp_table[1] = 1
root_n = int(n**0.5)

if root_n**2 == n:
    sprint(str(1)+'\n')
else:
    for i in range(2,n+1):
        root_i = int(i**0.5)
        if root_i**2 == i:
            dp_table[i] = 1
            continue
        for j in range(1, int(i**0.5)+1):
            dp_table[i] = min(dp_table[i], 1 + dp_table[i-j**2])
    sprint(str(dp_table[n])+'\n')
'''
print('time', time.time() - start)


