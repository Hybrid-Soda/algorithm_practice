# 1486 장훈이의 높은 선반

import sys
sys.stdin = open('input.txt')

def comb(i, sum_v):
    global ans
    if sum_v >= B:
        sub = sum_v - B
        ans = min(ans, sub)
        return

    if i < N:
        comb(i+1, sum_v)
        comb(i+1, sum_v+height[i])

for tc in range(int(input())):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    ans = B
    comb(0, 0)
    print(f'#{tc+1}', ans)