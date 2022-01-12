# 1463th, 1로 만들기 | class 3
import time

start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

# DP bottom-up

N = int(input())
count_list = [0] * N


for x in range(2, N+1):
    div_3 = count_list[x//3-1] if not x % 3 else sys.maxsize
    div_2 = count_list[x//2-1] if not x % 2 else sys.maxsize
        
    count_list[x-1] = 1 + min(div_3, div_2, count_list[x-2])

print(count_list[N-1])

# 참조 답
# 심플
'''
s={1:0,2:1}
def f(n):
 if n in s:return s[n]
 m=1+min(f(n//2)+n%2,f(n//3)+n%3)
 s[n]=m
 return m
print(f(int(input())))
'''

# 참조 답
# DP top-down, Set 사용
'''
l={int(input())};n=0
while 1 not in l:
	t=set();n+=1
	for i in l:
		if i%3==0:t.add(i//3)
		if i%2==0:t.add(i//2)
		t.add(i-1)
	l=t
print(n)
'''

# DP top-down 함수형
# 재귀 초과, 메모리 초과로 테스트 힘듬
'''
import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

sys.setrecursionlimit(1000000)
def reduct_to_one(n:int, cl: list):
    if n == 1: return 0

    div_3 = sys.maxsize if n % 3 else cl[n//3-1] if cl[n//3-1] else reduct_to_one(n//3, cl)
    div_2 = sys.maxsize if n % 2 else cl[n//2-1] if cl[n//2-1] else reduct_to_one(n//2, cl)
    sub_1 = cl[n-2] if cl[n-2] != 0 else reduct_to_one(n-1, cl)
    cl[n-1] = 1 + min(div_3, div_2, sub_1)

    return cl[n-1]
    
N = int(input())
count_list = [0] * N

print(reduct_to_one(N, count_list))
'''

# DP 사용안함 -> 안됨
'''
def reduct_to_one(n:int):
    if n == 1: return 0
    A, B, C, D, E = 0, 0, 1, sys.maxsize, sys.maxsize
    while C <= n:
        C *= 3
        A += 1
    A = n-C//3 + A-1
    C = 1
    while C <= n:
        C *= 2
        B += 1
    B = n-C//2 + B-1
    C = sys.maxsize
    if not n % 3:
        C = reduct_to_one(n//3) + 1
    if not n % 2:
        D = reduct_to_one(n//2) + 1

    E = reduct_to_one(n-1) + 1

    return min(A,B,C, D, E)

N = int(input())

print(reduct_to_one(N))
'''

print('time', time.time() - start)


