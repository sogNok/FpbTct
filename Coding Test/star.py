# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:23:29 2021

@author: 이충섭
"""
import copy
from itertools import permutations

#N, M = map(int, input().split())
#N_play = list(map(int, input().split()))
#M_play = list(map(int, input().split()))

N = 50
M = 50
print('done1')
N_play = [i for i in range(50)]
M_play = [i for i in range(49,-1,-1)]
N_perm = [0 for _ in range(N)]
print('done2')

#%%
for i in range(N):
    print(i)
    A = [1 for _ in range(N_play[i])]
    B = [0 for _ in range(M-N_play[i])]
    N_perm[i] = sorted(list(set(permutations(A + B, M)))) 

# Number of games exceeded
if len(N_play) > M or len(M_play) > N:
    print(-1)
    exit(0)
# Games not established
if sum(N_play) != sum(M_play):
    print(-1)
    exit(0)

match_table = [(0) for row in range(M)]


def Create_match(row):
    if row == N:
        return True
    
    # Reset tmp_play
    tmp_play = copy.deepcopy(M_play)
    for i in range(row):
        for j in range(M):
            if match_table[i][j] == 1:
                tmp_play[j] -= 1
    
    itr_col = len(N_perm[row]) - 1
                
    # Main loop
    while True:
        # Check if a row's match table is possible
        while itr_col >= 0:
            for i in range(N_play[row]):
                if N_perm[row][itr_col][i] == 1 and tmp_play[i] == 0:
                    break
            else:
                break
            
            itr_col -= 1
            if itr_col < 0:
                return False
        
        # Set Match Table for Row
        match_table[row] = copy.deepcopy(N_perm[row][itr_col])
        
        if Create_match(row+1):
            return True
        else:
            itr_col -= 1
            if itr_col < 0:
                return False
            
            # Termination condition
            if sum(tmp_play) < N_play[row]:
                return False
            
            # Clear tmp_table
            match_table[row] = 0
    
if Create_match(0):
    for i in range(N):
        for j in range(M):
            print(match_table[i][j], end='')
        print()

else:
    print(-1)
