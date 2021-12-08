# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 22:25:02 2021

@author: 이충섭
"""

# 10809th, 알파벳 찾기 | class 1

lower_string = input()

for alphabet in range(ord('a'), ord('z') + 1):
    locate = lower_string.find(chr(alphabet))
    print(locate, end=' ')
    
    
