# 16236 아기상어

import sys
from collections import deque
sys.stdin = open('input.txt')

# 초기 위치 확인
def search():
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 9: return i, j

def BFS(ci, cj, size):
    Q = deque([[ci, cj, 0]])
    visit = [[0] * N for _ in range(N)]
    fishes = []

    while Q:
        i, j, dist = Q.popleft()
    
        for di, dj in go:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and visit[ni][nj] == 0 and grid[ni][nj] <= size:

                # 여기 수정 (가능한 물고기 모두 리스트에 저장 후 정렬 -> 맨 앞의 물고기 선택)
                if 0 < grid[ni][nj] < size:
                    d = abs(i-ni) + abs(j-nj)
                    fishes.append([d, nj, -ni])
                    grid[ci][cj] = 0
                    grid[ni][nj] = 9
                    return ni, nj, dist+1

                visit[ni][nj] = 1
                Q.append([ni, nj, dist+1])
    return False

for _ in range(int(input())):
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    go = ((-1, 0), (0, 1), (0, -1), (1, 0))
    time, size, food = 0, 2, 2
    i, j = search()

    while True:
        result = BFS(i, j, size)

        if not result:
            break
        else:
            i, j, dist = result
            time += dist
            food -= 1

        if not food:
            size += 1
            food = size

    print(time)

# 답 : 0 3 14 60 48 39