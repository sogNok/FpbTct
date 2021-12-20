# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:20:53 2021

@author: 이충섭
"""

# 11651st, 좌표 정렬하기 2 | class 2

import sys # int(sys.stdin.readline().r l strip()) sys.stdout.write()

lst = sys.stdin.readlines()[1:]

lst.sort(key=lambda x: int(x.split()[0]))
lst.sort(key=lambda x: int(x.split()[1]))
print(''.join(lst))
