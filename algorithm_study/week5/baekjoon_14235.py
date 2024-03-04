# 14235 크리스마스 선물

import sys
sys.stdin = open('input.txt')
import heapq

gift = []
for _ in range(int(input())):
    n = list(map(int, input().split()))
    if n.pop(0):
        heapq.heappush(gift, n)
    else:
        if gift: print(-heapq.heappop(gift))
        else: print(-1)