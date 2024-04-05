# 15681 트리와 쿼리

import sys
sys.stdin = open('input.txt')

def DFS(now):
    visit[now] = 1
    for next in tree[now]:
        if not visit[next]:
            DFS(next)
            subtree[now] += subtree[next]
    
    subtree[now] = 1
    return

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
visit = [0] * (N+1)
subtree = [0] * (N+1)

for _ in range(N-1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

DFS(R)

[print(subtree[int(input())]) for _ in range(Q)]