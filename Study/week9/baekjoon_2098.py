# 2098 외판원 순회

import sys
from heapq import heappush, heappop
sys.stdin = open("input.txt")

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 16000000

for i in range(N):
    cost = 0
    visit = [0] * N
    Q = [[0, i]]

    while Q:
        w, now = heappop(Q)
        cost += w
        visit[now] = 1

        Q = []

        for next in range(N):
            if arr[now][next] and not visit[next]:
                heappush(Q, [arr[now][next], next])

        if not Q:
            cost += arr[now][i]
            break

    if 0 not in visit:
        ans = min(ans, cost)

print(ans)

'''
순열로 완전탐색 할 시 -> 20922789888000 번 계산 해야함
'''