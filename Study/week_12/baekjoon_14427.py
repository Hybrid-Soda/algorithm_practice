# 14427 수열과 쿼리 15

class LinkArr:
    def __init__(self, n, i):
        self.n = n
        self.i = i
    
    def __str__(self):
        return f'{self.n}'

import sys
from heapq import heappop, heappush
sys.stdin = open('input.txt')


N = int(input())  # 1 <= N <= 100,000
A = list(map(int, input().split()))  # 1 <= A <= 10^9
tree = []

for i in range(N):
    heappush(tree, LinkArr(A[i], i).n)

for _ in range(int(input())):  # 1 <= M <= 100,000
    query = list(map(int, input().split()))
    print(tree)
    if query[0] == 1:
        A[query[1]-1] = query[2]
    else:
        print(tree[0][1])