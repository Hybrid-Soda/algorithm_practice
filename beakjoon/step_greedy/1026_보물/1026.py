# 1026 보물
# S의 최솟값 출력

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

N = input()
A = sorted(map(int, input().split()), reverse=True)
B = sorted(map(int, input().split()))
C = list(zip(A, B))

S = 0
for a, b in C:
    S += a * b

print(S)