'''
<벨만-포드 알고리즘>
그래프에서 한 정점에서 다른 모든 정점까지의 최단 경로를 찾는 알고리즘
이 알고리즘은 음의 가중치를 가진 간선이 있어도 사용할 수 있으며, 음의 사이클이 있는지도 판별할 수 있다.
모든 간선을 확인하면서, 시작점에서 해당 간선을 거쳐 다른 정점으로 가는 거리가
현재 알려진 최단 거리보다 짧은지 검사하고, 필요한 경우 업데이트한다.
'''

def bellman_ford(V, edges, start):
    # 거리 테이블 초기화
    dist = [float('inf')] * (V+1)
    dist[start] = 0

    # V-1 + 1번 반복
    for i in range(V):
        for u, v, w in edges:

            # 정점 u까지의 거리가 이미 계산되었는지 확인하고
            # u를 거쳐 v로 가는 경로가 현재 알려진 v까지의 최단 거리보다 더 짧은지 검사
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

                # 이때도 값의 업데이트가 있다면 음의 사이클이 있는 것
                if i == V-1:
                    return None

    return dist