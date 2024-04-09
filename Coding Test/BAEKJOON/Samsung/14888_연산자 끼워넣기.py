# 14888th, 연산자 끼워넣기 | Samsung

import time

start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

def equation(answer,i,p,m,t,d):
    global max_val, min_val
    
    if i == N:
        max_val = max(max_val, answer)
        min_val = min(min_val, answer)
        return
    
    if p:
        equation(answer+seires[i],i+1,p-1,m,t,d)
    if m:
        equation(answer-seires[i],i+1,p,m-1,t,d)
    if t:
        equation(answer*seires[i],i+1,p,m,t-1,d)
    if d:
        if answer < 0:
            equation(abs(answer)//seires[i]*-1,i+1,p,m,t,d-1)
        else:
            equation(answer//seires[i],i+1,p,m,t,d-1)
    
    
N = int(sinput())
seires = list(map(int, sinput().split()))
op_list = list(map(int, sinput().split()))

max_val = -sys.maxsize
min_val = sys.maxsize

equation(seires[0],1,*op_list)

print(max_val)
print(min_val)
