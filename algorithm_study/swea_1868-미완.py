# 1868 파핑파핑 지뢰찾기
# 인접한 8칸에 폭탄이 없는 곳이면 8칸 통째로 1개
# 심지어 그 다음 칸도 인접 8칸이 비어있으면 연쇄적으로 터짐
# 인접한 8칸에 폭탄이 있으면 그 칸만 1개

import sys
sys.stdin = open("input.txt")


# 인접한 8칸에 지뢰나 0가 있는지 체크
def check_bomb(board, i, j, di, dj):
    is_mine = False; is_zero = False

    # 8방뱡 탐색
    for k in range(8):
        ni = i + di[k]; nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj] == '0':
                is_zero = True
            elif board[ni][nj] == '*':
                is_mine = True
    
    # 주변에 지뢰가 없으면 0 체크
    if not is_mine:
        board[i][j] = '0'

    return is_zero


# 클릭 개수 세기
def click_count(N, board):
    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]
    cnt = 0

    # board 탐색
    for i in range(N):
        for j in range(N):
            # 지뢰부분이면 다음으로 이동
            if board[i][j] == '*':
                continue

            # 지뢰와 0 체크
            is_zero = check_bomb(board, i, j, di, dj)

            # 주변에 0이 없으면 인접 8칸까지 클릭한 효과
            if not is_zero:
                cnt += 1
            # 주변에 지뢰가 있으면 클릭한번에 그 칸만 클릭
            
    return cnt


for tc in range(int(input())):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    
    
    print(f'#{tc+1} {click_count(N, board)}')