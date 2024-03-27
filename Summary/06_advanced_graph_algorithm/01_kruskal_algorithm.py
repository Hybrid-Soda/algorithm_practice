'''
    <크루스칼(Kruskal) 알고리즘>
    가중치 그래프의 모든 정점을 최소 비용으로 연결하는 최소 신장 트리(MST)를 찾는 알고리즘
    간선을 가중치의 오름차순으로 정렬한 다음, 가장 가중치가 낮은 간선부터 선택하면서 트리를 구성
    유니온-파인드(Union-Find) 자료구조를 사용하여 사이클을 감지하고 처리
'''

# 노드의 루트 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# 두 집합을 병합하는 함수
def union(x, y):
        if rank[x] > rank[y]:
            parent[y] = x
        elif rank[x] < rank[y]:
            parent[x] = y
        else:
            parent[y] = x
            rank[x] += 1

def kruskal(graph):
    # 최소 신장 트리(MST) 저장 리스트 초기화
    mst = []
    # 그래프의 간선들을 가중치에 따라 오름차순으로 정렬
    edges = sorted(graph['edges'], key=lambda x: x[2])

    # 모든 간선에 대해 반복
    for edge in edges:
        x, y, weight = edge
        # 각 정점의 루트 찾기
        root1 = find(x)
        root2 = find(y)

        # 두 정점이 서로 다른 집합에 속해있다면 (사이클을 형성하지 않는다면)
        if root1 != root2:
            # 간선 선택
            mst.append(edge)
            # 두 집합 병합
            union(root1, root2)

    # 완성된 MST 반환
    return mst

V = 10
parent = list(range(V))
rank = [0] * V
