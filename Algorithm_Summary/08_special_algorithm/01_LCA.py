'''
    <최소 공통 조상(Lowest Common Ancestor, LCA)>
    두 노드의 최소 공통 조상을 찾는 기본적인 알고리즘
    1. 각 노드의 부모 노드 정보를 저장
    2. DFS를 활용하여 각 노드의 깊이(depth)와 각 노드의 부모 노드 정보를 계산
    3. 두 노드의 깊이를 맞춘 후 조상을 찾아 올라가며 LCA를 찾는다
'''

n = 10  # 노드 개수
tree = [[] for _ in range(n + 1)]  # 트리
depth = [0] * (n + 1)  # 각 노드의 깊이
parent = [0] * (n + 1)  # 각 노드의 부모 노드

# DFS를 활용하여 각 노드의 깊이와 부모를 설정하는 함수
def DFS(now, d, par):
    depth[now] = d
    parent[now] = par
    for next_node in tree[now]:
        if next_node != par:
            DFS(next_node, d + 1, now)

# LCA를 찾는 함수
def LCA(a, b):
    # 두 노드의 깊이를 맞춤
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 공통 조상 검색
    while a != b:
        a = parent[a]
        b = parent[b]
    return a