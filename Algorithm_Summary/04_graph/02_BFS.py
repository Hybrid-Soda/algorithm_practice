'''
    <너비 우선 탐색(Breadth-First Search, BFS)>
    그래프의 모든 노드를 방문하고자 할 때 사용하는 알고리즘
    시작 노드로부터 가까운 노드를 먼저 방문하고
    멀리 떨어진 노드를 나중에 방문하는 방식
    BFS는 주로 큐(Queue)를 사용하여 구현
'''

from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    # 큐가 비어있지 않는 동안
    while queue:
        now = queue.popleft()

        # 방문하지 않은 노드라면
        if now not in visited:
            visited[now] = 1
            # 큐에 인접노드 추가
            queue.extend([next for next in graph[now] if not visited[next]])