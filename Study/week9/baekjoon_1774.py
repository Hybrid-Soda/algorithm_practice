# 1774 우주신과의 교감
# 최소 스패닝 트리 (MST) - 간선의 개수가 매우 많으므로 프림 알고리즘 사용

import sys
sys.stdin = open('input.txt')
from heapq import heappush, heappop

n, m = map(int, input().split())
pos = [list(map(int, input().split())) for _ in range(n)]
adj = [[0] * n for _ in range(n)]

for i in range(n-1):
    for j in range(i, n):
        x1, y1 = pos[i]
        x2, y2 = pos[j]
        dist = ((x1-x2)**2 + (y1-y2)**2)**0.5
        adj[i][j] = dist
        adj[j][i] = dist

sum_weight = 0
MST = [0] * n
Q = []

for _ in range(m):
    i, j = map(int, input().split())
    adj[i-1][j-1] = adj[j-1][i-1] = 0

heappush(Q, (0, 0))
while Q:
    weight, now = heappop(Q)

    if MST[now]: continue

    MST[now] = 1
    sum_weight += weight

    for next in range(n):
        if now != next and not MST[next]:
            heappush(Q, (adj[now][next], next))

print(sum_weight)