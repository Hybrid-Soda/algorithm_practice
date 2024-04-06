# 13335 트럭

import sys
from collections import deque
sys.stdin = open('input.txt')

# 트럭 수, 다리 길이, 다리의 최대 하중
N, W, L = map(int, input().split())
trucks = deque(list(map(int, input().split())))
bridge = deque([0] * W, maxlen=W)  # 최대값을 가지는 큐 생성
load = 0
time = 0

while trucks or load:
    time += 1
    load -= bridge.popleft()

    if trucks:
        if load + trucks[0] <= L:
            bridge.append(trucks.popleft())
            load += bridge[-1]
        else:
            bridge.append(0)

print(time)