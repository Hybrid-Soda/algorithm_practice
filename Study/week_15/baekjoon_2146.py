# 2146 다리만들기
# BFS 

import sys
sys.stdin = open('input.txt')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

print(board)