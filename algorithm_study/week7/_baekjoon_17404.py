# 17404 RGB 거리 2 (골드4)

import sys 
sys.stdin = open('input.txt') 

N = int(input())
rgb = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N-1):
    for j in range(3):
        rgb[i][j] += min(rgb[i-1][j-1], rgb[i-1][j-2])

temp = sorted(rgb[0][:])
min_i = rgb[0].index(temp[0])

for i in range(3):
    rgb[-1][i] += min(rgb[-2][i-1], rgb[-2][i-2])
    if i == min_i: rgb[-1][i] += temp[1] - temp[0]

print(min(rgb[-1]))