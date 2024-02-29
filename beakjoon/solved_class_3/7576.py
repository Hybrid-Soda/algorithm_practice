# 7576 토마토

import sys
sys.stdin = open("input.txt")
from collections import deque

ds = [(0, 1), (1, 0), (0, -1), (-1, 0)]

M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]
Q = deque([[i, j, 0] for i in range(N) for j in range(M) if tomato[i][j] == 1])

while Q:
    i, j, d = Q.popleft()
    for di, dj in ds:
        ni, nj = i + di, j + dj
        if 0<=ni<N and 0<=nj<M and tomato[ni][nj] == 0:
            Q.append([ni, nj, d+1]); tomato[ni][nj] = 1

if any(0 in row for row in tomato): print(-1)
else: print(d)
