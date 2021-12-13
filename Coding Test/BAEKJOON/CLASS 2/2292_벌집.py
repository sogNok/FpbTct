# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 10:56:27 2021

@author: 이충섭
"""

# 2292nd, 벌집 | class 2


# 6의 배수로 증가하는 계차수열 문제
# 58 -> 56 -> 9 | 62 -> 60 -> 10
N = int(input())
N_ = N - 2
N__ = N_ // 6

# 0부터 시작하는 계차수열 (n 찾기)
# x = n(n+1) / 2 | -1 ~ N__ = N__ + 1 => 2(N__ + 1) == n(n+1)
# 9 -> 20 | 10 -> 22
N__ += 1
N__ *= 2

# 가까운 수를 찾기 위한 제곱근 + 버림
# 20 -> 4 | 22 -> 4
sqrt_N = pow(N__, 1/2)
count = int(sqrt_N)

# 소속 계차수열 구간 찾기
# 0 = 0 | 1, 2 = 1 | 3, 4, 5 = 3 | ...
# (20)9 <= 4 * 5 -> 4구간 | (22)10 <= 5*6 -> 5구간
while True:
    if N__ <= count * (count+1):
        break
    count += 1

# 처음과 끝을 포함하니 +1
# 4 -> 5칸, 5-> 6칸
print(count + 1)

#%%
# 참조 답
# 난 시간초과뜨던데 ㅠ => 실수
sum = 1
n = int(input())
for k in range(0,1000000001):
    sum += (6 * k)
   
    if sum >= n:
        print(k + 1)
        break
    
#%%

N = int(input())
N_ = N - 2
N__ = N_ // 6


i = 0
while N__ > -1:
    i += 1
    N__ -= i

print(i+1)