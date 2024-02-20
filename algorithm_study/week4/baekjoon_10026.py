# 10226 / 적록색약 /골드5

import sys
sys.stdin = open('input.txt')
from collections import deque

def search(i, j, a, weakness):
    if not weakness: global cnt; cnt += 1
    else: global w_cnt; w_cnt += 1

    Q = deque([[i, j]])
    while Q:
        i, j = Q.popleft()
        for di, dj in dr:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N:
                if pic[ni][nj] == a:
                    if weakness:
                        pic[ni][nj] = 0
                    else:
                        if a == 'R':
                            pic[ni][nj] = 'g'
                        else:
                            pic[ni][nj] = a.lower()
                    Q.append([ni, nj])

dr = [(0, 1), (1, 0), (0, -1), (-1, 0)]
N = int(input())
pic = [list(input()) for _ in range(N)]
cnt, w_cnt = 0, 0

for i in range(N):
    for j in range(N):
        for char in ['R', 'G', 'B']:
            if pic[i][j] == char:
                search(i, j, char, False)

for i in range(N):
    for j in range(N):
        for char in ['r', 'g', 'b']:
            if pic[i][j] == char:
                search(i, j, char, True)

print(cnt, w_cnt)