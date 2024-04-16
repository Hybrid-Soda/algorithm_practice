# 1799 비숍

import sys
sys.stdin = open('input.txt')

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[1-board[i][j] for j in range(N)] for i in range(N)]

go = ((1, 1), (1, -1), (-1, 1), (-1, -1))
ans = 0

def check(i, j, put):
    visit[i][j] += 2*put - 1
    for k in range(1, N):
        for di, dj in go:
            ni = i + k*di
            nj = j + k*dj
            if 0 <= ni < N and 0 <= nj < N:
                visit[ni][nj] += 2*put - 1

def DFS(ni, nj, cnt):
    global ans
    if cnt + (N - ni) <= ans:
        return

    for i in range(ni, N):
        for j in range(nj, N):
            if not visit[i][j]:
                check(i, j, 1)
                DFS(i, j, cnt+1)
                check(i, j, 0)
        nj = 0
    ans = max(ans, cnt)

DFS(0, 0, 0)
print(ans)