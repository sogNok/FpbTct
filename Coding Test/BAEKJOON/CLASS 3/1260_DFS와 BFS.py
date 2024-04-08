# 1260th, DFS와 BFS | class 3

import time

start = time.time()
# print('time', time.time() - start)

from collections import deque
import copy
import sys
sinput = sys.stdin.readline
sprint = sys.stdout.write


def dfs(node, adj_mat, answer):
    stack = []
    visited = [False] * len(adj_mat)
    #visited[V] = True
    stack.append(V)
    
    while stack:
        node = stack.pop()
        
        if not visited[node]:
            answer.append(str(node))
            visited[node] = True
        
            for index in range(len(visited)-1,0,-1):
                if adj_mat[node][index] and not visited[index]:
                    stack.append(index)
            
def bfs(V, adj_mat, answer):
    queue = deque()
    visited = [False] * len(adj_mat)
    visited[V] = True
    queue.append(V)
    
    while queue:
        node = queue.popleft()
        answer.append(str(node))
        
        for index, next_node in enumerate(adj_mat[node]):
            if next_node and not visited[index]:
                visited[index] = True
                queue.append(index)
    
N, M, V = map(int, sinput().split())
adj_mat = [[False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    i, j = map(int, sinput().split())
    adj_mat[i][j] = True
    adj_mat[j][i] = True

answer = []
dfs(V, adj_mat, answer)
sprint(' '.join(answer) + '\n')

answer = []
bfs(V, adj_mat, answer)
sprint(' '.join(answer) + '\n')
