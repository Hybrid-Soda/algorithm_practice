"""
    <위상 정렬(topological sorting)>
    유향 그래프의 노드들을 간선의 방향을 거스르지 않도록 나열하는 것
    - 선후 관계가 정의된 그래프 구조 상에서 선후 관계에 따라 정렬하기 위해 위상 정렬을 이용할 수 있다.
    - 주로 선수 과목을 정하는 문제나 작업 스케줄링 문제에 사용
    사이클이 없는 방향 그래프(DAG, Directed Acyclic Graph)
    - 위상 정렬이 성립하기 위해서는 반드시 그래프의 순환이 존재하지 않아야 한다.

    수행과정
    1. 자기 자신을 가리키는 간선이 없는 노드를 찾음
    2. 찾은 노드를 출력하고 출력한 노드와 그 노드에서 출발하는 간선을 삭제
    3. 아직 그래프에 노드가 남아있으면 단계 1로 돌아가고, 아니면 알고리즘을 종료
"""

from collections import deque

N = 6  #  노드 개수
relations = [(1, 4), (5, 4), (4, 3), (2, 5), (2, 3), (6, 2)]  # (선수 노드, 후수 노드)

graph = [[] for _ in range(N + 1)]  # 그래프 초기화
in_degree = [0] * (N + 1)  # 각 노드의 진입 차수

# 그래프 생성 및 진입 차수 계산
for pre, post in relations:
    graph[pre].append(post)
    in_degree[post] += 1


# 위상 정렬 - Kahn 알고리즘
def topological_sort():
    result = []
    Q = deque()

    # 처음 시작할 때 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            Q.append(i)

    # 큐가 빌 때까지 반복
    while Q:
        now = Q.popleft()
        result.append(now)

        # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
        for next in graph[now]:
            in_degree[next] -= 1

            # 새롭게 진입 차수가 0이 되는 노드를 큐에 삽입
            if in_degree[next] == 0:
                Q.append(next)

    # 위상 정렬을 수행한 결과 출력
    print(*result)

topological_sort()