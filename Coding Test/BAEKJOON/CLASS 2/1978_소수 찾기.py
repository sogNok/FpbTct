
# 1978th, 소수 찾기 | class 2

import sys

N = int(sys.stdin.readline())

num_list = list(map(int, sys.stdin.readline().split()))

count = 0
for num in num_list:
    is_divisible = 0

    for x in range(1, num+1):
        if num % x == 0:
            is_divisible += 1

    if is_divisible == 2: count += 1

sys.stdout.write(str(count))

'''
# 참조 답
# 중간에 멈추기

n=int(input())
li=list(map(int,input().split()))
cnt=0
for i in li:
    f=True
    if i<=1:continue
    for j in range(2,i):
        if i%j==0:
            f=False
            break
    if f:
        cnt+=1
print(cnt)