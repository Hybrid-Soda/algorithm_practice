'''
<A* (A-star) 알고리즘>
최단 경로를 찾는 효율적인 그래프 탐색 알고리즘
다익스트라 알고리즘을 기반으로 하지만, '휴리스틱'이라는 추정 함수를 추가하여
더 빠르게 목표지점까지의 최적 경로를 찾습니다.
핵심 : 각 단계에서 현재 정점에서 목표지점까지의 총 예상 비용이 가장 낮은 정점을 선택하는 것
[비용]
- g(n) : 시작 정점에서 현재 정점 n까지의 실제 비용
- h(n) : 현재 정점 n에서 목표 정점까지의 추정 비용(휴리스틱 비용)
- f(n) : 총 비용, f(n) = g(n) + h(n)
[휴리스틱 함수]
- 2차원 격자에서의 최단 경로 문제에서는 '맨해튼 거리'나 '유클리드 거리'가 휴리스틱 함수로 자주 사용
- 휴리스틱 함수의 선택에 따라 성능이 크게 달라질 수 있다.
'''

from heapq import heappush, heappop

def a_star(start, goal, h, graph):
    # 오픈 세트 초기화: 시작 정점과 시작 정점의 휴리스틱 비용을 포함
    open_set = [(h(start), start)]
    # 각 정점의 이전 정점을 추적
    came_from = {}
    # 시작 정점에서 각 정점까지의 실제 비용
    g_score = {start: 0}
    # 각 정점까지의 예상 총 비용
    f_score = {start: h(start)}

    while open_set:
        # 오픈 세트에서 가장 낮은 f(n) 값을 가진 정점을 추출
        now_f, now = heappop(open_set)

        # 목표 정점에 도달했다면, 경로를 재구성하여 반환
        if now == goal:
            path = []
            while now in came_from:
                path.append(now)
                now = came_from[now]
            path.append(start)
            return path[::-1]

        # 현재 정점 이웃 정점 탐색
        for next in graph(now):
            # 이웃까지의 거리를 가정 (예시 1)
            assume_g_score = g_score[now] + 1

            # 더 좋은 경로를 발견했다면 g_score, f_score를 업데이트하고 오픈 세트에 추가
            if next not in g_score or assume_g_score < g_score[next]:
                came_from[next] = now
                g_score[next] = assume_g_score
                f_score[next] = assume_g_score + h(next)
                heappush(open_set, (f_score[next], next))
    
    return None

# 휴리스틱 함수 1 : 맨해튼 거리
def manhattan_distance(now, goal):
    return abs(now[0] - goal[0]) + abs(now[1] - goal[1])

# 휴리스틱 함수 2 : 유클리드 거리
def get_neighbors(now):
    dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    result = []
    for d in dir:
        next = (now[0] + d[0], now[1] + d[1])
        if 0 <= next[0] < 5 and 0 <= next[1] < 5:
            result.append(next)
    return result