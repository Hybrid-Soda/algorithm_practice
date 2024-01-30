# 1961 숫자 배열 회전
import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    
    arr_90 = [[0] * N for _ in range(N)]
    arr_180 = [[0] * N for _ in range(N)]
    arr_270 = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N-1-j][i]
    
    for i in range(N):
        for j in range(N):
            arr_180[i][j] = arr_90[N-1-j][i]
    
    for i in range(N):
        for j in range(N):
            arr_270[i][j] = arr_180[N-1-j][i]
    
    print(f'#{tc}')
    for i in range(N):
        print(''.join(arr_90[i]), ''.join(arr_180[i]), ''.join(arr_270[i]))