# 2357 최솟값과 최댓값

import sys
sys.stdin = open('input.txt')

INF = float('inf')
N, M = map(int, input().split())
max_tree = [0 for _ in range(2*N)]
min_tree = [INF for _ in range(2*N)]

# 트리 삽입
for i in range(N):
    num = int(input())
    max_tree[N+i] = num
    min_tree[N+i] = num

# 트리 정렬
for i in range(N-1, 0, -1):
    max_tree[i] = max(max_tree[i<<1], max_tree[i<<1|1])
    min_tree[i] = min(min_tree[i<<1], min_tree[i<<1|1])

# 쿼리 수행
for _ in range(M):
    a, b = map(int, input().split())
    a += N-1
    b += N-1
    maxV = 0
    minV = INF

    while a < b:
        if a & 1:
            pass
        if ~(b & 1):
            pass
        a >>= 1
        b >>= 1
    
    if a == b:
        maxV = max(maxV, max_tree[a])
        minV = min(minV, min_tree[a])
    
    print(minV, maxV)