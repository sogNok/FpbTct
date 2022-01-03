# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 20:50:05 2021

@author: 이충섭
"""

# 1874th, 스택 수열 | class 2

import sys

n = int(next(sys.stdin))

output = []
stack = []
last_num = 0

for num_str in sys.stdin:
    num = int(num_str)
    
    if num > last_num:
        for x in range(last_num + 1, num + 1):
            output.append('+')
            stack.append(x)
            
        last_num = num
        
    elif num != stack[-1]:
        output = ['NO']
        break
    
    output.append('-')
    stack.pop()

sys.stdout.write('\n'.join(output))

#%%
# 참조 답
# 알고리즘은 같지만 더 편한 사용법

import sys
input = sys.stdin.read


def sol1874():
    n, *nums = map(int, input().split())
    cur = 1
    st = []
    answer = []
    for num in nums:
        while cur <= num:
            st.append(cur)
            answer.append('+')
            cur += 1
        if st[-1] != num:
            answer = ['NO']
            break
        st.pop()
        answer.append('-')
    print('\n'.join(answer))
   

if __name__ == '__main__':
    sol1874()