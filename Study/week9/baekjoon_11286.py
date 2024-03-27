# 11286 절대값 힙

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

Q = []
for _ in range(int(input())):
    x = int(input())
    if x: heappush(Q, [abs(x), x//abs(x)])
    else:
        if Q: x, y = heappop(Q); print(x*y)
        else: print(0)