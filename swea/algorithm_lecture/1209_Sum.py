# 1209 Sum

import sys
sys.stdin = open("input.txt")

for tc in range(10):
    case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    turn_arr = [[0] * 100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            turn_arr[i][j] = arr[99-j][i]
    row_max = 0
    col_max = 0
    cross1 = 0
    cross2 = 0

    # 각 행의 합
    for row in arr:
        row_max = max(row_max, sum(row))

    # 각 열의 합
    for col in turn_arr:
        col_max = max(col_max, sum(col))

    # 각 대각선의 합
    for i in range(100):
        cross1 += arr[i][i]
        cross2 += arr[i][99-i]
    
    print(f'#{case} {max(row_max, col_max, cross1, cross2)}')



