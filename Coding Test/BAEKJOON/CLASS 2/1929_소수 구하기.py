# 1929th, 소수 구하기 | class 2
import time
start = time.time()

import sys
import bisect
sinput = sys.stdin.readline
sprint = sys.stdout.write

M, N = map(int, input().split())

prime_list = [True for _ in range(N+1)]
prime_list[0] = False
prime_list[1] = False

for x in range(2, int(N**0.5) + 1):
    if prime_list[x]:
        itr = x+x
        while itr <= N:
            prime_list[itr] = False
            itr += x

for itr in range(M, N+1):
    if prime_list[itr]:
        sprint(str(itr)+'\n')


'''
# 소수를 찾은 후 위치 검색
prime_list = []

for num in range(2, N+1):
    limit = num ** 0.5 + 1
    for prime in prime_list:
        if not num % prime:
            break
        elif limit < prime:
            prime_list.append(num)
            break
    else:
        prime_list.append(num)

sprint('\n'.join(map(str, prime_list[bisect.bisect_left(prime_list, M):])))
'''
'''
# 느리고 간단한 답
for num in range(M, N+1):
    limit = math.isqrt(num)
    for x in range(2, limit+1):
        if not num % x:
            break
    else:
        sprint(str(num)+'\n')
'''
print('time', time.time() - start)