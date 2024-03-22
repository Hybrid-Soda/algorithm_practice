'''
<플로이드 워셜(Floyd-Warshall) 알고리즘>
모든 쌍의 최단 경로를 찾는 알고리즘
그래프 내의 모든 정점들 사이의 최단 거리를 계산
음의 가중치가 있어도 작동하지만, 음의 사이클이 있으면 정확한 결과를 제공할 수 없다.

핵심 : 모든 정점을 한 번씩 "중간 정점"으로 고려하면서, 해당 정점을 경유하는 것이
두 정점 사이의 거리를 줄일 수 있는지 검사하고, 가능하다면 거리를 업데이트하는 것
'''

def floyd_warshall(V, graph):
    # 거리 테이블 초기화
    dist = [[float('inf')] * V for _ in range(V)]

    # 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(V):
        dist[i][i] = 0

    # 간선의 가중치로 초기화
    for u, v, w in graph:
        dist[u][v] = w

    # 플로이드 워셜 알고리즘 적용 - k: 중간, i: 출발, j: 도착
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist