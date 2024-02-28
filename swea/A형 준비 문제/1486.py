# 1486 장훈이의 높은 선반

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N, B = map(int, input().split())
    L = tuple(map(int, input().split()))
    T = sum(L) - B
    max_s = 0
    stack = [(0, 0)]
    while stack:
        i, sum_v = stack.pop()
        max_s = max(max_s, sum_v)
        if i < N:
            stack.append((i + 1, sum_v))
            if sum_v + L[i] <= T:
                stack.append((i + 1, sum_v + L[i]))
    print(f'#{tc+1}', T - max_s)

'''
def comb(sum_v, i):
    global min_v
    if min_v <= sum_v:
        return
    if sum_v >= B:
        min_v = min(min_v, sum_v)
        return
    if i < N:
        comb(sum_v + H[i], i+1)
        comb(sum_v, i+1)

for tc in range(int(input())):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    min_v = 10000*N
    comb(0, 0)
    print(f'#{tc+1} {min_v-B}')
'''