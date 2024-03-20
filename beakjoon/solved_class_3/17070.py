# 17070 파이프 옮기기 1

import sys
sys.stdin = open("input.txt")

N = int(input())
M = [list(map(int, input().split())) for _ in range(N)]
DP = [[[0] * 3 for _ in range(N)] for _ in range(N)]

for j in range(1, N):
    if M[0][j]: break
    DP[0][j][0] = 1

for i in range(1, N):
    for j in range(1, N):
        now = M[i][j]; up = M[i-1][j]; left = M[i][j-1]; cross = M[i-1][j-1]
        if not (now or left):  # 옆
            DP[i][j][0] = DP[i][j-1][0] + DP[i][j-1][1]
        if not (now or left or cross or up):  # 대각
            DP[i][j][1] = DP[i-1][j-1][0] + DP[i-1][j-1][1] + DP[i-1][j-1][2]
        if not (now or up):  # 위
            DP[i][j][2] = DP[i-1][j][1] + DP[i-1][j][2]

print(sum(DP[-1][-1]))