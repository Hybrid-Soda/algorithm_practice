# 15650 N과 M(2)

from itertools import combinations

N, M = map(int, input().split())
for i in combinations([i for i in range(1, N+1)], M):
    print(*i)