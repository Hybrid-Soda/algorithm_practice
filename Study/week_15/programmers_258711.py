# 도넛과 막대 그래프 (2024 KAKAO WINTER INTERNSHIP)

from collections import deque

def BFS(start):
    visit = {start, }
    Q = deque([start])

def solution(edges):
    graph = [[] for _ in range(len(edges)+1)]

    for s, e in edges:
        graph[s].append(e)
    
    return graph

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]])) # [2, 1, 1, 0]