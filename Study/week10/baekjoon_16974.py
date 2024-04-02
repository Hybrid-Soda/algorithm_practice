# 16974 레벨 햄버거
#  Lv |   Thickness   |     patty     |
# -------------------------------------
#  0  |  1            |  1            |
#  1  |  5 = 3 + 2*1  |  3 = 1 + 2*1  |
#  2  | 13 = 3 + 2*5  |  7 = 1 + 2*3  |
#  3  | 29 = 3 + 2*13 | 15 = 1 + 2*7  |
#  4  | 61 = 3 + 2*29 | 31 = 1 + 2*15 |
#  5  |125 = 3 + 2*61 | 63 = 1 + 2*31 |
# 패티가 항상 햄버거번보다 한장 더 많다.

import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, X = map(int, input().split())

burger = [1] * (N+1)
patty = [1] * (N+1)

for i in range(1, N+1):
    burger[i] = 3 + 2 * burger[i-1]
    patty[i] = 1 + 2 * patty[i-1]

def search(N, X):
    if not N:
        return 1

    mid = burger[N]//2 + 1
    if X == mid:
        return 1
    elif X > mid:
        return search(N-1)
    else:
        return search(N-1, )