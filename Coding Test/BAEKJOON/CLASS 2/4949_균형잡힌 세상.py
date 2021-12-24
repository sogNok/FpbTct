# 4949th, 균형잡힌 세상 | class 2

import sys
input_str = []
left_bracket = ('(', '{', '[')
right_bracket = (')', '}', ']')

while True:
    input_str.append(sys.stdin.readline().rstrip())

    if input_str[-1] == '.':
        input_str.pop()
        break

for line in input_str:
    stack = []

    for alpha in line:
        if alpha in left_bracket:
            stack.append(alpha)
        elif alpha in right_bracket:
            if not stack:
                print('no')
                break
            else:
                ralpha = stack.pop()
                if ralpha == '(' and alpha == ')' or ralpha == '{' and alpha == '}' or ralpha == '[' and alpha == ']':
                    pass
                else:
                    print('no')
                    break
        else: pass
    else:
        if stack: print('no')
        else: print('yes')

'''
# 참조 답
# 보다 간단
from sys import stdin, stdout

def isvalid(s):
    stack = []
    for c in s:
        if c in '([':
            stack.append(c)
        elif c == ')':
            if not stack or stack.pop() != '(':
                return False
        elif c == ']':
            if not stack or stack.pop() != '[':
                return False
    return not stack

strings = stdin.readlines()
strings.pop()
for string in strings:
    stdout.write("yes\n" if isvalid(string) else "no\n")
'''