# 4835 구간합

import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    # 정수의 개수 : N / 구간의 개수 : M
    N, M = map(int, input().split())
    # 숫자 배열
    arr = list(map(int, input().split()))
    sum_arr = []

    # 정수 개수 - 구간 개수 + 1 만큼 순회
    for i in range(N-M+1):
        # 순회하며 더한 숫자 값을 sum_arr에 추가
        sum_arr.append(sum(arr[i:i+M]))

    # 더한 값의 최대값과 최소값의 차를 출력
    print(f'#{tc} {max(sum_arr) - min(sum_arr)}')