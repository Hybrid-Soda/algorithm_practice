# 16928 뱀과 사다리 게임

import sys
sys.stdin = open("input.txt")
from collections import deque

warp = {int(x[0]): int(x[1]) for x in [input().split() for _ in range(sum(map(int, input().split())))]}
Q, dist = deque([1]), [0] * 101

while Q:
    now = Q.popleft()
    if now == 100: print(dist[100]); break
    for i in range(1, 7):
        next = now + i
        if next <= 100 and not dist[next]:
            if next in warp.keys():
                dist[next] = dist[now] + 1
                next = warp[next]
            if not dist[next]: dist[next] = dist[now] + 1
            Q.append(next)