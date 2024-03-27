T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # + 모양
    for i in range(N):
        for j in range(N):
            temp = arr[i][j]
            for k in range(1, M):
                if i+k < N:
                    temp += arr[i+k][j]
                if i-k >= 0:
                    temp += arr[i-k][j]
                if j+k < N:
                    temp += arr[i][j+k]
                if j-k >= 0:
                    temp += arr[i][j-k]
            if temp > ans:
                ans = temp

    # x 모양
    for i in range(N):
        for j in range(N):
            temp = arr[i][j]
            for k in range(1, M):
                if i+k < N and j+k < N:
                    temp += arr[i+k][j+k]
                if i+k < N and j-k >= 0:
                    temp += arr[i+k][j-k]
                if i-k >= 0 and j+k < N:
                    temp += arr[i-k][j+k]
                if i-k >= 0 and j-k >= 0:
                    temp += arr[i-k][j-k]
            if temp > ans:
                ans = temp
                
    print(f'#{tc} {ans}')