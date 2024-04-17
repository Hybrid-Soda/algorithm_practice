# 17141 연구소 2

from collections import deque
from itertools import combinations

go = ((1, 0), (0, 1), (-1, 0), (0, -1))
N, M = map(int, input().split())
LAB = [list(map(int, input().split())) for _ in range(N)]
FLU = []

for i in range(N):
    for j in range(N):
        if LAB[i][j] == 0:
            LAB[i][j] = -1
        elif LAB[i][j] == 2:
            FLU.append([i, j])
            LAB[i][j] = -1
        else:
            LAB[i][j] = -2

def BFS(FLU):
    sec = 0
    LAB2 = [l[:] for l in LAB]
    for i, j in FLU:
        LAB2[i][j] = 0
    Q = deque(FLU)

    while Q:
        i, j = Q.popleft()
        for di, dj in go:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and LAB2[ni][nj] == -1:
                LAB2[ni][nj] = LAB2[i][j] + 1
                Q.append([ni, nj])
    print(LAB2)

    for i in range(N):
        for j in range(N):
            if LAB2[i][j] == -1:
                return ans
            sec = max(sec, LAB2[i][j])

    return sec

ans = float('inf')
for f in combinations(FLU, M):
    ans = min(ans, BFS(f))

print(-1 if ans == float('inf') else ans)