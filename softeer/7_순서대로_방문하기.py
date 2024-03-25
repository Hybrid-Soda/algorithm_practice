# [HSAT 7회 정기 코딩 인증평가 기출] 순서대로 방문하기

def dfs(now, destIdx):
    global cnt
    if now == dest[destIdx]:
        if destIdx == n-1:
            cnt += 1
            return
        else:
            destIdx += 1
    
    x, y = now
    visit[x][y] = True

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == False and grid[x][y] == 0:
            dfs([nx, ny], destIdx)
    
    visit[x][y] = False
    return

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dest = []

for _ in range(m):
    x, y = map(int, input().split())
    dest.append([x-1, y-1])
visit = [[False for _ in range(n)] for _ in range(n)]

cnt = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dfs(dest[0], 1)
print(cnt)