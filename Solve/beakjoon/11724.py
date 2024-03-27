# 11724 연결 요소의 개수

import sys
sys.stdin = open("input.txt")
from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
ans = 0

for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        Q = deque([i])
        while Q:
            now = Q.popleft()
            visited[now] = 1
            for next in graph[now]:
                if not visited[next]:
                    Q.append(next)
                    visited[next] = 1
        ans += 1
print(ans)

