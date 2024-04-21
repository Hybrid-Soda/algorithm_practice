# 1199 오일러 회로

import sys
sys.stdin = open('input.txt')

N = int(input())
route = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]
stack = []

for i in range(N):
    for j in range(i):
        if route[i][j]:
            graph[i].append(j)
            graph[j].append(i)
    if sum(route[i]) & 1: exit(print(-1))

while stack:
    now = stack[-1]

    while graph[now]:
        next = graph[now][-1]
        now, next = now, next if now <= next else next, now

        if route[now][next]:
            break
        else:
            graph[now].pop()

    if len(graph[now]):
        route[now][next] -= 1
        stack.append(next)
    else:
        stack.pop()
        print(next+1, end=' ')

'''
    - 오일러 경로 : 그래프의 모든 간선을 정확히 한 번씩 지나는 경로
    - 오일러 회로 : 오일러 경로 + 시작점이 종료점과 같음

    - Euler's Theorem
        1. 홀수 차수를 가지는 정점이 0 or 2개인 경우 오일러 경로를 적어도 1개 갖는다.
        2. 모든 정점이 짝수 차수를 가지는 경우 오일러 회로를 적어도 1개 갖는다.

    - 오일러 회로 찿기 - Hierholzer Algorithm
        1. 시작 노드 v를 선택하고 v에서 v로 돌아갈 때까지 간선 궤적을 따른다
        2. 
'''