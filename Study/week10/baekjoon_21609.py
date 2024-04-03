# 21609 상어 중학교
import sys
sys.stdin = open('input.txt')

def DFS(arr, i, j, color):
    visit = []
    S, cnt, r_cnt = [[i, j]], 0, 0
    base = [N, N]
    while S:
        i, j = S.pop()
        if arr[i][j]:
            base = min(base, [i, j])
        for di, dj in go:
            ni, nj = i + di, j + dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] in [0, color] and [ni, nj] not in visit:
                visit.append([ni, nj])
                cnt += 1
                if not arr[ni][nj]: r_cnt += 1
                S.append([ni, nj])
    return cnt, r_cnt, base, visit

def find_group(arr):
    max_group = [0, 0, [0, 0]]
    groups = []
    for i in range(N):
        for j in range(N):
            if 0 < arr[i][j] <= M:
                cnt, r_cnt, base, visit = DFS(arr, i, j, arr[i][j])
                if cnt < 2: continue
                if max_group < [cnt, r_cnt, base]:
                    max_group = [cnt, r_cnt, base]
                    groups = visit
    if max_group == [0, 0, [0, 0]]: return
    for i, j in groups:
        arr[i][j] = M+1
    return max_group[0]

def gravity(arr):
    for i in range(N-2, -1, -1):
        for j in range(N):
            if 0 <= arr[i][j] <= M:
                temp = arr[i][j]; arr[i][j] = M+1; ni = i
                while ni < N-1 and arr[ni+1][j] == M+1: ni += 1
                arr[ni][j] = temp

def turn(arr):
    new_arr = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[j][N-i-1]
    return new_arr

go = ((1, 0), (0, 1), (0, -1), (-1, 0))
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
ans = 0

while True:
    B = find_group(grid)  # 블록 그룹 찾기
    if not B: exit(print(ans))  # 종료
    ans += B**2  # 합산
    gravity(grid)  # 중력
    grid = turn(grid)  # 회전
    gravity(grid)  # 중력