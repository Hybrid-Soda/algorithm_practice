# 5650 핀볼 게임

import sys 
sys.stdin = open('input.txt') 

def collision(r, c, d):
    global score; score += 1
    cell = board[r][c]
    if d == 0:  # UP
        if (cell == 0 and r == 0) or cell in [1, 4, 5]: d = 1
        elif cell == 2: d = 3
        elif cell == 3: d = 2
    elif d == 1:  # DOWN
        if (cell == 0 and r == N-1) or cell in [2, 3, 5]: d = 0
        elif cell == 1: d = 2
        elif cell == 4: d = 3
    elif d == 2:  # LEFT
        if (cell == 0 and r == 0) or cell in [3, 4, 5]: d = 3
        elif cell == 1: d = 0
        elif cell == 2: d = 1
    else:  # RIGHT
        if (cell == 0 and r == N-1) or cell in [1, 2, 5]: d = 2
        elif cell == 3: d = 1
        elif cell == 4: d = 0
    return d

def wormhole(r, c):
    for i in range(N):
        for j in range(N):
            if (i != r and j != c) and board[i][j] == cell:
                return i, j

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

for tc in range(int(input())):
    N, score = int(input()), 0
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = {}
    cnt = 0

    for r in range(N):
        if cnt >= 50: break
        for c in range(N):
            rr, rc = r, c
            for d in range(4):
                rr = r; cc = c; dd = d
                # 종료 : 블랙홀로 이동
                while board[rr][cc] != -1:
                    cnt += 1
                    cell = board[rr][cc]
                    # 점수 획득, 방향 변경: 벽이나 블록에 충돌
                    if -1 < cell < 6:
                        dd = collision(rr, cc, dd)
                    # 순간 이동: 웜홀로 이동
                    elif 5 < cell < 11:
                        rr, cc = wormhole(rr, cc)
                    # 일반 이동
                    rr += dr[dd]; cc += dc[dd]
                    # 종료 : 출발위치로 이동
                    if rr == r and cc == c:
                        break
                    # 지나간 경로에 대한 점수 : visited에 키는 시작 위치 및 방향, 값은 점수 저장

    print(f'#{tc+1}', score)

