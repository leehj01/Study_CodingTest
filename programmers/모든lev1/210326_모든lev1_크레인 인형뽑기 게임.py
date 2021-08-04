# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.7.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

# +
from collections import deque

def solution(board, moves):
    baguni = []
    for m in moves:
        for i in range(len(board)):
            if board[i][m -1 ] != 0:
                baguni.append(board[i][m-1])
                board[i][m-1] = 0
                break

    realbaguni = deque(baguni)
    b = []
    cnt = 0
    for i in range(len(realbaguni)):
        tmp = realbaguni.popleft()
        if not b or b[-1] != tmp:
            b.append(tmp)
        else :
            b.pop()
            cnt += 2
    return cnt
