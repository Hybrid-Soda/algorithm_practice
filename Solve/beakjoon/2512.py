# 2512 예산

N = int(input())
cost = list(map(int, input().split()))
M = int(input())
low, high = 0, max(cost)

# 찾아야 하는 요인을 조정하며 이분탐색
while low <= high:
    mid = (high+low) // 2
    total = sum(mid if c > mid else c for c in cost)

    if total <= M: low = mid + 1
    else: high = mid - 1

print(high)