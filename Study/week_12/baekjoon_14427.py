# 14427 수열과 쿼리 15

import sys
sys.stdin = open('input.txt')

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
qry = [list(map(int, input().split())) for _ in range(m)]

tree = [None] * (4*n)

def init(node, start, end):
    if start == end:
        tree[node] = (arr[start], start+1)
    else:
        mid = (start + end) // 2
        init(node*2, start, mid)
        init(node*2+1, mid+1, end)
        tree[node] = min(tree[node*2], tree[node*2+1], key=lambda x: (x[0], x[1]))

init(1, 0, n-1)

def update(node, start, end, idx, value):
    if start == end:
        tree[node] = (value, idx + 1)
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update(node*2, start, mid, idx, value)
        else:
            update(node*2+1, mid+1, end, idx, value)
        tree[node] = min(tree[node*2], tree[node*2+1], key=lambda x: (x[0], x[1]))

result = []
query_index = 0

for _ in range(m):
    query_type = int(qry[query_index])
    if query_type == 1:
        idx = int(qry[query_index + 1]) - 1
        value = int(qry[query_index + 2])
        update(1, 0, n-1, idx, value)
        query_index += 3
    elif query_type == 2:
        result.append(str(tree[1][1]))
        query_index += 1

    print("\n".join(result))