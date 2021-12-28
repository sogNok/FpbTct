# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 15:48:25 2021

@author: 이충섭
"""

# 11866th, 요세푸스 문제 0 | class 2

N, K = map(int, input().split())

josephus = [x for x in range(1, N+1)]
len_per = len(josephus)
itr = K - 1

print('<', end='')
while josephus:
    # start condition
    itr %= len_per
    
    print(josephus.pop(itr), end=', ') if len_per > 1 else print(josephus.pop(itr), end='>')
    
    
    # end condition
    itr += K - 1
    len_per -= 1
    
#%%
# 참조 답
# join 활용

N, K = map(int, input().split())
l = list(range(1, N+1))
p = list()
i = 0
while l:
    i = (i+K-1) % len(l)
    p.append(str(l.pop(i)))

print('<'+', '.join(p)+'>')