# 1012th, 유기농 배추 | class 3

import time

start = time.time()
# print('time', time.time() - start)

import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write

def dfs(i, j, cabbage_mat):
    global N, M
    stack = []
    cabbage_mat[i][j] = 0
    stack.append((i,j))
    
    while len(stack):
        i,j = stack.pop()
        
        if i+1 < N and cabbage_mat[i+1][j]:
            cabbage_mat[i+1][j] = 0
            stack.append((i+1,j))
        
        if j+1 < M and cabbage_mat[i][j+1]:
            cabbage_mat[i][j+1] = 0
            stack.append((i,j+1))

        if i-1 >= 0 and cabbage_mat[i-1][j]:
            cabbage_mat[i-1][j] = 0
            stack.append((i-1,j))
            
        if j-1 >= 0 and cabbage_mat[i][j-1]:
            cabbage_mat[i][j-1] = 0
            stack.append((i,j-1))
    

T = int(sinput())
answer = []

for _ in range(T):
    M, N, K = map(int, sinput().split())
    cabbage_mat = [[0] * M for _ in range(N)]
    count = 0
    
    for _ in range(K):
        j, i = map(int, sinput().split())
        cabbage_mat[i][j] = 1
    
    for i in range(N):
        for j in range(M):
            if cabbage_mat[i][j] == 1:
                dfs(i, j, cabbage_mat)
                count += 1
                
    answer.append(str(count))
    
sprint('\n'.join(answer))
