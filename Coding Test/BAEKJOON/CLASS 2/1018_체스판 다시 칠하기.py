# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 00:00:25 2021

@author: 이충섭
"""

# 1018th, 체스판 다시 칠하기 | class 2

W = 'WBWBWBWB'
B = 'BWBWBWBW'

# White First Chess Board
WB = [W if x % 2 == 0 else B for x in range(8)]
# Black First Chess Board
BB = [B if x % 2 == 0 else W for x in range(8)]

# Check num of difference between window board and base board
def redrawNum(window_board, base_board):
    num = 0
    for i in range(8):
        for j in range(8):
            if window_board[i][j] != base_board[i][j]:
                num += 1
    return num
    
H, W = map(int, input().split())
input_CB = [input() for _ in range(H)]

min_list = []

# Check num of difference by sliding window
for i in range(H-7):
    for j in range(W-7):
        window_CB = [ row[j:j+8] for row in input_CB[i:i+8] ]
        min_num = min(redrawNum(window_CB, WB), redrawNum(window_CB, BB))
        min_list.append(min_num)

print(min(min_list))