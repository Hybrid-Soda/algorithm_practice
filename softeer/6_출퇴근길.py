# [HSAT 6회 정기 코딩 인증평가 기출] 출퇴근길

def dfs(now, adj, visit):
    if visit[now]: return
    visit[now] = 1
    for next in adj[now]: dfs(next, adj, visit)

n, m = map(int, input().split())
adj = [[] for _ in range(n+1)]
adjR = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = map(int, input().split())
    adj[s].append(e)
    adjR[e].append(s)

s, t = map(int, input().split())

fromS = [0] * (n+1); fromS[t] = 1
dfs(s, adj, fromS)  # 출발점에서 도착점으로

fromT = [0] * (n+1); fromT[s] = 1
dfs(t, adj, fromT)  # 도착점에서 출발점으로

toS = [0] * (n+1)
dfs(s, adjR, toS)  # 출발점에서 출발점으로

toT = [0] * (n+1)
dfs(t, adjR, toT)  # 도착점에서 도착점으로

# 출발점과 도착점으로 모두 갈 수 있는 노드의 개수 체크
count = 0
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]: count += 1
# 출발점과 도착점은 뺀다
print(count-2)

'''
    <관건>
    1. 출퇴근길에 모두 들를 수 있는 지점을 체크하는 것이므로 출근과 퇴근 모두 체크
    2. 거꾸로 가는 경로도 모두 체크
'''