# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 11:19:56 2021

@author: 이충섭
"""

# 1436th, 영화감독 숌 | class 2

import sys

N = int(input()) # int(sys.stdin.readline())
k = 0               # iteration number
layer = 1           # for count len of string | 1: x666 or 666x, 2: xx666 or x666x or 666xx
doom_list = [sys.maxsize for _ in range(54320)] # max num is lower than 54320 : 2*10 + 3*100 + 4*1000 + 5*10000


while N >= k:

    for x in range(layer + 1):                  # ex) 2: 0, 1, 2
        for pre_x in range(pow(10, layer-x)):   # ex) 2: 0-> 0~99, 1-> 0~9, 2-> 0(=X)
            
            for post_x in range(pow(10, x)):    # ex) 2: 0-> '', 1-> 0~9, 2-> 0~99 
                if x == 0: post_x = ''
                doom_list[k] = int(str(pre_x) + '666' + str(post_x).zfill(x))
                k += 1
    layer += 1

doom_list = list(set(doom_list))
doom_list.sort()
print(doom_list[N-1])    