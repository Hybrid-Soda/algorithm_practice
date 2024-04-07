'''
    <프림 알고리즘(Prim's algorithm)>
    그래프에서 최소 신장 트리를 찾는 알고리즘
    가중치가 있는 무방향 그래프에 대해 작동하며,
    각 단계에서 신장 트리 집합에 추가될 최소 가중치 간선을 선택한다.
'''

from heapq import heappush, heappop

def prim(graph, start, V):
    sum_weight = 0  # 최소 비용 합계
    MST = [0] * V
    heap = []

    # 힙에서 관리해야 할 데이터 - 가중치, 정점 정보
    heappush(heap, (0, start))

    while heap:
        weight, v = heappop(heap)

        if MST[v]: continue  # 방문한 곳이라면 넘어감

        MST[v] = 1
        sum_weight += weight  # 누적합에 합산

        for next in range(V):
            # 갈 수 있고 방문하지 않은 노드라면 힙에 추가
            if graph[v][next] and not MST[next]:
                heappush(heap, (graph[v][next], next))

    return MST, weight