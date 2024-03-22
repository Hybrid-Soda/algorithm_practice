# [HSAT 6회 정기 코딩 인증평가 기출] 출퇴근길
# 목표 : 목표노드에 도착하기까지 도착할 수 있는 모든 노드 찾기

import sys
sys.stdin = open("input.txt")

def DFS(visited, now, end):
    if now != end and not graph[now]:
        return False
    
    if now == end:
        return True

    for next in graph[now]:
        if not visited[next]:
            visited[next] = 1
            if not DFS(visited, next, end):
                visited[next] = 0

    return True


N, M = map(int, input().split())  # 정점 개수, 간선 개수
graph = [[] for _ in range(N+1)]  # 유향 그래프
visited = [0] * (N+1)  # 방문 목록

# 그래프 제작
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)

S, T = map(int, input().split())  # 시작 정점, 도착 정점

DFS(visited, S, T)
print(visited)
'''
    <간과한 부분>
    1. 만약 도착지점이 아닌데 더 이상 연결 노드가 없으면 퇴근길에 들르는 노드가 아니다
    2. 8 -> 9 이런 끝 부분이 있을 수 있으므로 이건 무조건 DFS로 해야 할듯
        시작 지점에서 도착 지점에 도착하면 그 때 카운트 하는 걸로
'''