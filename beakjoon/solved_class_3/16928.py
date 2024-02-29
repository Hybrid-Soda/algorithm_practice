# 16928 뱀과 사다리 게임

import sys
sys.stdin = open("input.txt")
from collections import deque

N, M = map(int, input().split())  # 사다리 수, 뱀의 수
ladder = [tuple(map(int, input().split())) for _ in range(N)]
snake = [tuple(map(int, input().split())) for _ in range(M)]
dist = [1, 1] + [0] * 99
print(ladder)

Q = deque([1])
while Q:
    n = Q.popleft()
    dist
    for i in range(1, 7):
        next = n + i
        # 사다리
        if next:
            pass
        # 뱀
        elif next:
            pass
        else:
            Q.append()
            