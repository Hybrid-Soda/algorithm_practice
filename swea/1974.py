# 스도쿠 검증

T = int(input())

def check_arr(arr, ans):
    for i in range(9):
        if len(set(arr[i])) != 9:
            ans = 0
            break
    return ans

for tc in range(1, T+1):
    ans = 1
    arr_1 = [list(map(int, input().split())) for _ in range(9)]
    arr_2 = [[0]*9 for _ in range(9)]
    arr_3 = [[] for _ in range(9)]

    # 세로 줄
    for i in range(9):
        for j in range(9):
            arr_2[i][j] = arr_1[9-1-j][i]

    # 3x3 격자
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            arr_3[i + j//3].extend(arr_1[i][j:j+3])
            arr_3[i + j//3].extend(arr_1[i+1][j:j+3])
            arr_3[i + j//3].extend(arr_1[i+2][j:j+3])
    
    # 가로 줄 확인
    ans = check_arr(arr_1, ans)

    # 세로 줄 확인
    if ans == 1:
        ans = check_arr(arr_2, ans)

    # 3x3 격자 확인
    if ans == 1:
        ans = check_arr(arr_3, ans)

    print(f'#{tc} {ans}')