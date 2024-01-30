# 1979 어디에 단어가 들어갈 수 있을까
# NxN 크기의 단어 퍼즐
# 주어진 퍼즐 모양에서 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수 출력

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, K = map(int, input().split())
    puzzle = [input().split() for _ in range(N)]
    ans = 0

    for i in range(N):
        count = 0
        # 행 검사
        for j in range(N):
            # 현재 칸의 숫자가 1이라면 카운트
            if puzzle[i][j] == '1':
                count += 1

        # 열 검사
        for j in range(N):
            # 현재 칸의 숫자가 1이라면 카운트
            if puzzle[j][i] == '1':
                count += 1

    print(f'#{tc+1} {ans}')
