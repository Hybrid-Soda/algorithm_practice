# 1327 소트 게임

from collections import deque

N, K = map(int, input().split())
nums = tuple(map(int, input().split()))
sorted_nums = tuple(sorted(nums))
visit = {nums}

Q = deque([[nums[:], 0]])

while Q:
    nums, dist = Q.popleft()

    # 정렬된 순열과 같다면 종료
    if nums == sorted_nums:
        exit(print(dist))

    # 각 자리마다 뒤집은 배열 생성
    for i in range(N-K+1):
        next_nums = nums[:i] + nums[i:i+K][::-1] + nums[i+K:]
        if next_nums not in visit:
            visit.add(next_nums)
            Q.append([next_nums, dist+1])

# Q가 빌 때까지 종료가 안 되었다면 정렬이 불가능한 것
print(-1)