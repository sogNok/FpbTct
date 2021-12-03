# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 12:25:20 2021

@author: 이충섭
"""

# 1157th, 단어 공부 | class 1

''' 시간초과
alphabet_finder = input().upper()
max_apb = ''
max_num = 0
only_max = True

for apb in alphabet_finder:
    count = alphabet_finder.count(apb)
    
    if count > max_num:
        max_num = count
        max_apb = apb
        only_max = True
    elif count is max_num and max_apb is not apb:
        only_max = False
    
print(max_apb if only_max else '?')
'''

# only use A to Z = 65 to 90
upper_ascii = [0 for _ in range(26)]

max_apb = 0
max_num = 0
only_max = False

alphabet_finder = input().upper()

for apb in alphabet_finder:
    if apb.isupper():
        upper_ascii[ord(apb) - 65] += 1
    
for idx in range(26):
    
    if upper_ascii[idx] > max_num:
        max_num = upper_ascii[idx]
        max_apb = idx
        only_max = True

    elif upper_ascii[idx] == max_num:
        only_max = False
        
print(chr(max_apb + 65) if only_max else '?')