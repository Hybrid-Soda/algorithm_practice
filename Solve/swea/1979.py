import sys
sys.stdin = open('input.txt')

# 1979 어디에 단어가 들어갈 수 있을까
# NxN 크기의 퍼즐
# 특정 길이 K를 갖는 단어가 들어갈 수 있는 자리의 수를 출력

for tc in range(int(input())):
    N, K = map(int, input().split())
    ans = 0

    puzzle = []
    for row in range(N):
        puzzle.append(list(map(int, input().split())))

    turn_puzzle = [[0] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            turn_puzzle[row][col] = puzzle[N-1-col][row]
    
    for i in range(N):
        for j in range(N-2):
            count = 1
            s_count = 1
            # 1이 연속해서 3번 있는 조건
            if puzzle[i][j] == puzzle[i][j+1] == 1:
                count += 1
            else:
                count = 1
            if count == 3:
                ans += 1

            if puzzle[N-1-j][i] == puzzle[N-2-j][i] == 1:
                s_count += 1
            else:
                s_count = 1
            if s_count == 3:
                ans += 1

    print(f'#{tc} {ans}')