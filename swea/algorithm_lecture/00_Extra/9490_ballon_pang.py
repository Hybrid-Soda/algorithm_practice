# 9490 풍선팡
# 풍선이 NxM으로 있음
# 풍선을 터뜨리면 종이 꽃가루 개수만큼 상하좌우 풍선이 추가로 터짐
# 한 개의 풍선을 선택할 때 날릴 수 있는 꽃가루의 합 중 최대값을 출력

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 풍선 리스트 순회
    for i in range(N):
        for j in range(M):
            temp = arr[i][j]
            # 풍선 터뜨리기
            for k in range(1, temp+1):
                # 아래쪽 끝
                if i+k < N:
                    temp += arr[i+k][j]
                # 위쪽 끝
                if i-k >= 0:
                    temp += arr[i-k][j]
                # 오른쪽 끝
                if j+k < M:
                    temp += arr[i][j+k]
                # 왼쪽 끝
                if j-k >= 0:
                    temp += arr[i][j-k]
            ans = max(ans, temp)

    print(f'#{tc+1} {ans}')
