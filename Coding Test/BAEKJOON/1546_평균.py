# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 12:26:04 2021

@author: 이충섭
"""

# 1546th, 평균 | class 1

NUM_SUBJECT = int(input())

subjects = [0 for _ in range(NUM_SUBJECT)]

instance_subject = input().split()

for idx in range(NUM_SUBJECT):
    subjects[idx] = int(instance_subject[idx])
    
MAX_SCORE = max(subjects)
SUM_SCORE = sum(subjects)

False_avg = SUM_SCORE / (NUM_SUBJECT * MAX_SCORE) * 100

print(False_avg)