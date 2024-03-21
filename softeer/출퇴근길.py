# [HSAT 6회 정기 코딩 인증평가 기출] 출퇴근길

import sys
sys.stdin = open("input.txt")

from collections import deque

def BFS(S, T):
    visited = [0] * (N+1)
    Q = deque([S])
    while Q:
        now = Q.popleft()
        if now != T:
            visited[now] = 1
            for next in graph[now]:
                if graph[next] and not visited[next]:
                    Q.append(next)
    print(visited)
    return [i for i in range(N+1) if visited[i]]

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[e].append(s)

S, T = map(int, input().split())

print(len(set(BFS(S, T)) & set(BFS(T, S))))


'''
def DFS(visited, now, T):
    if now != T and not graph[now]:
        return False

    for next in graph[now]:
        visited[next] = 1
        if not DFS(visited, next, T):
            visited[next] = 0

    return True

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

S, T = map(int, input().split())
visited1 = [0] * (N+1); visited1[S] = visited1[T] = 1
visited2 = [0] * (N+1); visited2[S] = visited2[T] = 1

DFS(visited1, S, T); DFS(visited2, T, S); ans = 0
print(visited1); print(visited2)
for i in range(N+1):
    if not (i == S or i == T) and visited1[i] and visited2[i]:
        ans += 1

print(ans)
'''
'''
    <간과한 부분>
    1. 만약 도착지점이 아닌데 더 이상 연결 노드가 없으면 퇴근길에 들르는 노드가 아니다
    2. 8 -> 9 이런 끝 부분이 있을 수 있으므로 이건 무조건 DFS로 해야 할듯
        시작 지점에서 도착 지점에 도착하면 그 때 카운트 하는 걸로
'''