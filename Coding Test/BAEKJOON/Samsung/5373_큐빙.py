# 5373rd, 큐빙 | Samsung

import time

start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write


def T2L(T):
    L = []
    L.append(t[T[0]][T[1]])
    L.append(t[T[0]][T[2]])
    L.append(t[T[0]][T[3]])
    return L

def C2T(T, L):
    t[T[0]][T[1]] = L[0]
    t[T[0]][T[2]] = L[1]
    t[T[0]][T[3]] = L[2]
    
def turn(way, sign):
    target = t[way]
    
    if sign == '+':
        last = target.pop()
        target.insert(0,last)
        last = target.pop()
        target.insert(0,last)
        
        last_list = T2L(relation[way][-1])
        for x in relation[way]:
            temp_list = T2L(x)
            C2T(x, last_list)
            last_list = temp_list
        
    elif sign == '-':
        first = target.pop(0)
        target.append(first)
        first = target.pop(0)
        target.append(first)
        
        last_list = T2L(relation[way][0])
        for x in reversed(relation[way]):
            temp_list = T2L(x)
            C2T(x, last_list)
            last_list = temp_list    

T = int(sinput())
result = []

for _ in range(T):
    n = int(sinput())
    direction = list(sinput().rstrip().split())
    
    t = {
    'U' : ['w'] * 8,
    'D' : ['y'] * 8,
    'F' : ['r'] * 8,
    'B' : ['o'] * 8,
    'L' : ['g'] * 8,
    'R' : ['b'] * 8,
    }

    relation = {
        'U' : [('B',2,1,0), ('R',2,1,0), ('F',2,1,0), ('L',2,1,0)],
        'D' : [('F',6,5,4), ('R',6,5,4), ('B',6,5,4), ('L',6,5,4)],
        'F' : [('U',6,5,4), ('R',0,7,6), ('D',2,1,0), ('L',4,3,2)],
        'B' : [('U',2,1,0), ('L',0,7,6), ('D',6,5,4), ('R',4,3,2)],
        'L' : [('U',0,7,6), ('F',0,7,6), ('D',0,7,6), ('B',4,3,2)],
        'R' : [('U',4,3,2), ('B',0,7,6), ('D',4,3,2), ('F',4,3,2)],
    }

    for d in direction:
        turn(d[0],d[1])
    
    result.append(t['U'][0:3])
    result.append(t['U'][7]+'w'+t['U'][3])
    result.append(t['U'][6:3:-1])

for x in result:
    sprint(''.join(x)+'\n')
