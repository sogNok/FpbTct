# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 22:20:04 2021

@author: 이충섭
"""

# Chapter 13 organization 1

with open('EoP_chap13_1.py', 'r', encoding='utf8') as f:
    for i, line in enumerate(f, 1):
        print(f'{i:04} {line}', end='')