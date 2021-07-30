# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 13:06:10 2021

@author: 이충섭
"""

# Chapter 08 organization

p1 = [75, 56, 89]   # English Score List
p2 = [42, 85, 77]   # Math Score List

# Dictionary with key last name and firt name value
name = {
    'Kim': 'seojun',
    'Lee': 'seoa',
    'Choi': 'hajun',
    }

# Zip to return the set(the elements of the set are Tupled)
plist = set(zip(name.items(), p1, p2))

# Output all elements of the set
for m in plist:
    print(m)