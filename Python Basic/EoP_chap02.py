# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 10:54:37 2021

@author: 이충섭
"""

print('ABC', 'XYZ')
print('ABC', 'XYZ', end='')     # 행의 마지막에서 개행하지 않음
print('ABC', 'XYZ', sep='')     # 구분을 위한 공백을 넣지 않음
print()                         # 개행
print('ABC\n\nXYZ', sep='')     # 중간에 두 번 개행
print()                         # 개행

s = input('문자열: ')
print('당신은', s, '을 입력하였습니다.')
print('당신은' + s + '을 입력하였습니다.')
print('당신은{}을 입력하였습니다.'.format(s))
print(f'당신은{s}을 입력하였습니다.')
print()

no = int(input('정수 값 : '))
print('마지막 자리의 값 : ', str(no % 10), sep='')
print('2진수: ' + bin(no))        # 2진 문자열로 변환
print('8진수: ' + oct(no))        # 8진 문자열로 변환
print('10진수: ' + str(no))       # 10진 문자열로 변환
print('16진수: ' + hex(no))       # 16진 문자열로 변환
print()

PI = 3.14159                    # 원주율을 나타내는 수
print('사각형과 원의 넓이를 구하겠습니다.')
width = float(input('사각형 가로의 길이 : '))
height = float(input('사각형 세로의 길이 : '))
radius = float(input('원의 반지름 : '))

print(f'사각형: {width * height}')
print(f'원:{PI * radius * radius}')