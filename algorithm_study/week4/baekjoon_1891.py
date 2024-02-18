# 1891 / 사분면 / 골드4

import sys
sys.stdin = open("input.txt")

def div_conq(n, i, j, quad):
    if len(quad) == d:
        arr[i][j] = quad
        return

    div_conq(n//2, i, j + n, quad + "1")
    div_conq(n//2, i, j, quad + "2")
    div_conq(n//2, i + n, j, quad + "3")
    div_conq(n//2, i + n, j + n, quad + "4")

d, num = map(int, input().split())
x, y = map(int, input().split())
N = int(4 ** (d / 2))
arr = [[0] * N for _ in range(N)]

div_conq(N//2, 0, 0, '')

for i in range(N):
    for j in range(N):
        if arr[i][j] == str(num):
            row, col = i, j
            break
try:
    print(arr[row-y][col+x])
except:
    print(-1)