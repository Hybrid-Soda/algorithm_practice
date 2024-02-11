# 11047 동전 0
# K원을 만들기 위한 동전의 최소 개수 구하기

import sys
sys.stdin = open("input.txt")

# N : 동전 종류 / K : 금액 합계
N, K = map(int, input().split())
cost = [int(input()) for _ in range(N)]
cnt = 0

for c in cost[::-1]:
    if K == 0:
        break
    if K >= c:
        cnt += K // c
        K %= c

print(cnt)