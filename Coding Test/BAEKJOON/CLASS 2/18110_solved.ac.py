# 18110th, solved.ac | class 2

import time

start = time.time()
# print('time', time.time() - start)

import sys

sinput = sys.stdin.readline
sprint = sys.stdout.write

EPS = 1e-9
N = int(sinput())
if N == 0:
    print(0)
else:
    cut_N = round(EPS + 3*N/20)
    
    input_list = [int(sinput()) for _ in range(N)] 
    input_list.sort()
    
    sprint(str(round(EPS + sum(input_list[cut_N:N-cut_N])/(N-2*cut_N))))
