# 3074 입국심사
# 이분 탐색을 통한 심사가 가능한 최소 시간 구함
# 전체 시간을 수렴시키며 각 심사대가 소화할 사람수 구함
# 핵심 : 인원 수를 조정하지 않고, 소요 시간을 조정하며 탐색

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N, M = map(int, input().split())  # 심사대, 사람수
    time = [int(input()) for _ in range(N)]  # 각 심사대 소요 시간
    left, right, ans = 1, max(time) * M, 0  # left: 최소 소요 시간 / right: 최대 소요 시간

    while left <= right:
        mid = (left + right) // 2  # 전체 심사 소요 시간
        people = sum([mid // t for t in time])  # 입국할 사람 수 (시간 별 해당 심사대가 소화하는 사람 수 배열 생성)
        print(f'심사대 당 소화 사람 수: {[mid // t for t in time]}')

        # 현재 사람 수가 목표 사람 수보다 많거나 같다면 최대 소요 시간을 줄임
        if people >= M:
            ans = mid
            right = mid - 1
        # 적다면 최소 소요 시간을 늘림
        else:
            left = mid + 1

    print(f'#{tc+1} {ans}')
