# 17406 배열돌리기4

import sys 
sys.stdin = open('input.txt') 

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

for _ in range(K):
    r, c, s = map(int, input().split())
print(A)