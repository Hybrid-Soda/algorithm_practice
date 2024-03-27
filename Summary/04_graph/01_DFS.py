'''
    <깊이 우선 탐색(Depth-First Search, DFS)>
    그래프의 깊은 부분을 우선적으로 탐색하는 알고리즘
    그래프의 모든 노드를 방문하고자 할 때 사용
    DFS는 재귀적으로 또는 명시적인 스택을 사용하여 구현
'''

# 재귀
def dfs(visited, graph, now):

    # 방문하지 않은 노드라면
    if not visited[now]:
        visited[now] = 1

        # 현재 노드의 인접 노드 탐색
        for next in graph[now]:
            dfs(visited, graph, next)

# 스택
def dfs_stack(graph, start, V):
    visited = [0] * (V+1)
    stack = [start]

    # 스택이 비어있지 않는 동안
    while stack:
        now = stack.pop()

        # 방문하지 않은 노드라면
        if not visited[now]:
            visited[now] = 1
            # 스택에 인접노드 추가
            stack.extend(reversed(graph[now]))