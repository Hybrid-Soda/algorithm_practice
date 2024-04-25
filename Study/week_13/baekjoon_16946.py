# 16946 벽 부수고 이동하기 4

import sys
from collections import deque
sys.stdin = open('input.txt')

go = ((0, 1), (1, 0), (0, -1), (-1, 0))
N, M = map(int, input().split())
grid = [list(map(int, input())) for _ in range(N)]

def empty(i, j):
    visit = [[0] * M for _ in range(N)]
    Q = deque([[i, j]])

    while Q:
        i, j = Q.popleft()
        for di, dj in go:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and not grid[ni][nj] and not visit[ni][nj]:
                visit[ni][nj] = 1
                Q.append([ni, nj])

for i in range(N):
    for j in range(M):
        if grid[i][j]:
            print(wall(), end='')
        else:
            empty(i, j)
            print(0, end='')
    print()