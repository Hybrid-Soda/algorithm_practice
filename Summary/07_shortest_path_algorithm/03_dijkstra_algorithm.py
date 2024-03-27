'''
<다익스트라 알고리즘>
그래프에서 한 정점에서 다른 모든 정점까지의 최단 경로를 찾는 알고리즘
음수 가중치를 갖는 간선이 없을 때 사용할 수 있다.
핵심 : 모든 정점을 순회하며, 각 단계에서 방문하지 않은 정점 중 가장 가까운 정점을 선택하고,
이 정점을 경유하여 다른 정점까지의 거리를 업데이트하는 것
'''

# heapqueue 없는 버전
def dijkstra(graph, start):
    V = len(graph)
    dist = [float('inf')] * V
    dist[start] = 0
    visited = [False] * V

    # 방문하지 않은 정점 중 가장 가까운 정점을 찾음
    for _ in range(V - 1):
        min_dist = float('inf')
        for v in range(V):
            if not visited[v] and min_dist > dist[v]:
                min_dist = dist[v]
                u = v
        visited[u] = True

        # 선택된 정점을 경유지로 해서 다른 정점까지의 거리를 업데이트
        for v in range(V):
            if not visited[v] and graph[u][v] and dist[v] > dist[u] + graph[u][v]:
                dist[v] = dist[u] + graph[u][v]

    return dist


# heapqueue 있는 버전 - 각 정점의 가장 가까운 정점을 빠르게 찾을 수 있으므로, 속도 향상
from heapq import heappush, heappop

def dijkstra_heap(graph, start):
    V = len(graph)
    dists = [float('inf')] * V
    dists[start] = 0
    Q = [(0, start)]

    while Q:
        now_dist, now = heappop(Q)

        # 이미 처리된 정점의 거리보다 긴 경우 스킵
        if dists[now] < now_dist:
            continue
        
        # 현재 노드에 연결된 노드 순회
        for next, weight in graph[now]:
            next_dist = now_dist + weight

            # 더 짧은 경로를 발견한 경우 업데이트하고 우선순위 큐에 추가
            if next_dist < dists[next]:
                dists[next] = next_dist
                heappush(Q, (next_dist, next))

    return dists

