# 4831 전기버스
# 전기버스 > 한번 충전으로 이동할 수 있는 정류장 수 정해져 있음
# 0에서 출발해서 종점인 N번 정류장까지 이동
# 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
# 충전기가 설치된 M개의 정류장 번호가 주어짐
# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지?
# 1. 최대한 진행하고 그 점에 충전기가 없으면 그 전에서 충전기 탐색
# 2. 그 충전기에서 부터 다시 카운트
# 3. 끝점까지 반복

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    # K: 한번 충전 최대 이동 거리 / N: 종점 / M: 충전기 설치 정류장 개수
    K, N, M = list(map(int, input().split()))
    # 충전기 설치 정류장
    charge = list(map(int, input().split()))
    # 충전 횟수
    ans = 0
    # 현 위치 (처음 진행한 이후부터 시작)
    pos = K
    # 이전 충전기 탐색
    neg = 0

    while pos < N:
        # 현 위치에 충전소가 있다면 충전 후 진행
        if pos in charge:
            ans += 1
            neg = 0
            pos += K
        # 현 위치에 충전소가 없다면 이전에서 충전기가 있는지 탐색
        else:
            pos -= 1
            neg += 1
        # 모두 탐색하였는데도 충전소가 없다면 0 출력
        if neg >= K:
            ans = 0
            break

    print(f'#{tc+1} {ans}')