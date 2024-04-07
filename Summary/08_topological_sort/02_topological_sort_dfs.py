"""
    DFS ver.
"""

N = 6  #  노드 개수
relations = [(1, 4), (5, 4), (4, 3), (2, 5), (2, 3), (6, 2)]  # (선수 노드, 후수 노드)

graph = [[] for _ in range(N + 1)]  # 그래프 초기화
visit = [False] * (N + 1)  # 방문 여부 체크
finish = [False] * (N + 1)  # 사이클 판단
stack = []
cycle = False

# 그래프 생성 및 진입 차수 계산
for pre, post in relations:
    graph[pre].append(post)


# 위상 정렬 - DFS
def DFS(now):
    visit[now] = True
    for next in graph[now]:
        # 방문하지 않았으면 DFS 실행
        if not visit[next]:
            DFS(next)
        # 방문하였는데 finish 체크가 되어있지 않다면 사이클 존재
        elif not visit[next]:
            global cycle
            cycle = True
            return

    # 끝에 도달했다면 스택에 추가
    finish[now] = True
    stack.append(now)


# 모든 노드에 대해 DFS 수행
for i in range(1, N + 1):
    if cycle:
        print('Cycle in graph!')
        break
    if not visit[i]:
        DFS(i)

# 위상 정렬을 수행한 결과 출력
while stack:
    print(stack.pop(), end=' ')
