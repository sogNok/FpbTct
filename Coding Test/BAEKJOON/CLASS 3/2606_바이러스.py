# 2606th, 바이러스 | class 3

import time

start = time.time()
# print('time', time.time() - start)

import sys

# dfs using stack
def dfs_1(visited, adj_mat):
    dfs_stack = [1]
    virus_count = 0
    visited[1] = True
    
    while dfs_stack:
        i = dfs_stack.pop()
        virus_count += 1
        
        for j in range(1,len(visited)):
            if adj_mat[i][j]:
                adj_mat[i][j] = False
                adj_mat[j][i] = False
                if not visited[j]:
                    dfs_stack.append(j)
                    visited[j] = True
        
    return virus_count

# dfs using recursion
def dfs_2(node, visited, adj_mat):
    virus_count = 1
    visited[node] = True
    
    for j in range(1,len(visited)):
        if adj_mat[node][j]:
            adj_mat[node][j] = False
            adj_mat[j][node] = False
            if not visited[j]:
                visited[j] = True
                virus_count += dfs_2(j, visited, adj_mat)
        
    return virus_count

from collections import deque

# bfs using queue
def bfs_1(visited, adj_mat):
    bfs_queue = deque([1])
    virus_count = 0
    visited[1] = True
    
    while bfs_queue:
        i = bfs_queue.popleft()
        virus_count += 1
        
        for j in range(1,len(visited)):
            if adj_mat[i][j]:
                adj_mat[i][j] = False
                adj_mat[j][i] = False
                if not visited[j]:
                    bfs_queue.append(j)
                    visited[j] = True
    return virus_count

    
sinput = sys.stdin.readline
sprint = sys.stdout.write

com_N = int(sinput())
N = int(sinput())

visited = [False] * (com_N+1)
adj_mat = [[False] * (com_N+1) for _ in range(com_N+1)]

for _ in range(N):
    i, j = map(int, sinput().split())
    adj_mat[i][j] = True
    adj_mat[j][i] = True
    
sprint(str(bfs_1(visited, adj_mat) - 1))
