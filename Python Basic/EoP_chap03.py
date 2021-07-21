# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 14:48:02 2021

@author: 이충섭
"""

a = int(input('정수 a: '))
b = int(input('정수 b: '))
c = int(input('정수 c: '))
d = int(input('정수 d: '))

if      a: print('a는 0이 아닙니다.')     # 0이 아니면 참
if not  b: print('b는 0 입니다.')        # 0이 아니면 참의 부정

# a, b, c 중에서 0이 아닌 첫 번쨰 값을 x에 대입하고, 모두 0인 경우 d를 x에 대입하기
x = a or b or c or d
print('x = ', x)

if d % c:                               # d를 c로 나눈 나머지가 0이 아니다.
    print('c는 d의 약수가 아닙니다.')
else:
    print('c는 d의 약수입니다.')
    
print('c는 ' + ('홀수' if c % 2 else '짝수') + '입니다.')

print('점수 d의 평가: ', end='')
if d < 0 or d > 100:    # 0~100 이외
    print('잘못된 점수')
elif d >= 60:
    print('합격')         # 60~100
else:
    print('불합격')        # 0~59