# 14500 테트로미노

import sys
sys.stdin = open("input.txt")

ds = ((0, 1), (1, 0), (-1, 0), (0, -1))

def DFS(d, i, j, sum_v):
    global max_v
    if sum_v + m * (4 - d) <= max_v: return
    elif d == 4: max_v = max(max_v, sum_v); return
    else:
        for di, dj in ds:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
                visited[ni][nj] = 1
                if d == 2:
                    DFS(d+1, i, j, sum_v+arr[ni][nj])
                DFS(d+1, ni, nj, sum_v+arr[ni][nj])
                visited[ni][nj] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited, max_v = [[0] * M for _ in range(N)], -1
m = max(map(max, arr))

for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        DFS(1, i, j, arr[i][j])
        visited[i][j] = 0

print(max_v)