# 11437 LCA (골드3)

import sys 
sys.stdin = open('input.txt') 

def find_p(n1, n2):
    parents = []
    while n1:
        parents.append(n1)
        n1 = tree[n1]
    while n2:
        if n2 in parents: return n2
        n2 = tree[n2]

N = int(input())
info = [tuple(map(int, input().split())) for _ in range(N-1)]
tree = [0] * (N+1)

while 0 in tree[2:]:
    for s, e in info:
        if tree[s] and tree[e]: pass
        elif tree[s] or s == 1: tree[e] = s
        elif tree[e] or e == 1: tree[s] = e

for _ in range(int(input())):
    print(find_p(*map(int, input().split())))


# 메모리 초과
'''
def find_p(n):
    p, parents = n, []
    while p:
        parents.append(p)
        p = tree[p]
    return parents

N = int(input())
info = [tuple(map(int, input().split())) for _ in range(N-1)]
tree = [0] * (N+1)

while 0 in tree[2:]:
    for s, e in info:
        if tree[s] and tree[e]: pass
        elif tree[s] or s == 1: tree[e] = s
        elif tree[e] or e == 1: tree[s] = e

for i in range(int(input())):
    n1, n2 = map(int, input().split())
    for j in find_p(n1):
        if j in find_p(n2): print(j); break
'''