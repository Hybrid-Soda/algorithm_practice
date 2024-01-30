# 2001 파리 퇴치
# MxM 크기의 파리채 / 최대한 많은 파리 죽이고자 함
# 5 <= N <= 15 / 2 <= M <= N / 각 영역의 파리 개수 30 이하

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for row in range(N-M+1):
        for col in range(N-M+1):
            temp = 0
            for i in range(M):
                for j in range(M):
                    temp += flies[row+i][col+j]
            ans = max(ans, temp)

    print(f'#{tc+1} {ans}')