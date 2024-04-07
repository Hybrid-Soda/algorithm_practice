"""
    <외판원 순회 문제(TSP, Traveling Salesman Problem)>
    여러 도시들이 있고 한 도시에서 다른 도시로 이동하는 비용이 모두 주어졌을 때,
    모든 도시들을 단 한 번만 방문하고 원래 시작점으로 돌아오는 최소 비용의 이동 순서를 구하는 것
    NP-난해 집합에 속하기 때문에 계산 이론에서 해를 구하기 어려운 문제의 대표적인 사례
    물류 및 배송 시스템 최적화, 순회 영업 직원의 경로 계획, 전자 회로 설계와 같은 다양한 분야에 활용
"""

from itertools import permutations

# 도시 간 거리를 나타내는 2차원 리스트
cost = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
N = len(cost)  # 도시 수
INF = float("inf")


# TSP - brute_force : O(n!) -> 매우 많은 시간을 요구
def TSP_brute_force():
    permu = permutations(range(N))  # 가능한 모든 경로의 순열 생성
    min_dist = INF
    min_path = None

    # 각 경로에 대해 거리 계산
    for path in permu:
        dist = 0

        ## 모든 도시 순회
        for next in range(N):
            dist += cost[path[next]][path[(next + 1) % N]]

        # 최소 거리 업데이트
        if dist < min_dist:
            min_dist = dist
            min_path = path

    # 최단 경로와 거리 반환
    return min_path, min_dist


# TSP - DP : O(n^2*2^n)
# DP[i][j] : i = 내 위치, j = 방문해야 하는 노드
DP = [[INF] * (2 << N) for _ in range(N)]


def TSP_DP(visit, now):
    # 모든 도시를 방문한 경우 비용 반환
    if visit == (1 << N) - 1:
        DP[now][visit] = cost[now][0]
        return cost[now][0]
    
    # 이미 계산된 경우
    if DP[now][visit] != INF:
        return DP[now][visit]

    # 모든 도시 순회
    for next in range(N):

        # 이미 방문한 도시면 패스
        if visit & (1 << next):
            continue

        # 다음 도시로 이동하는 비용 계산
        next_cost = cost[now][next] + TSP_DP(visit | (1 << next), next)
        DP[now][visit] = min(DP[now][visit], next_cost)

    return DP[now][visit]
