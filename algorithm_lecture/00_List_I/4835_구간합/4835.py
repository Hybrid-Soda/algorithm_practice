# 4835 구간합

import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    sum_arr = []

    for i in range(N-M+1):
        sum_arr.append(sum(arr[i:i+M]))

    print(f'#{tc} {max(sum_arr) - min(sum_arr)}')