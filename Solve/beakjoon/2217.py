# 2217 로프
# 들어올릴 수 있는 물체의 최대 중량 구하기

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
ropes = sorted([int(input()) for _ in range(N)])
weight = [ropes[i] * (N-i) for i in range(N)]
print(max(weight))