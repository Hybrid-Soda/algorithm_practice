# 3074 입국심사

import sys
sys.stdin = open("input.txt")

def f(i, d, sum_v):
    global min_v
    if sum_v >= min_v:
        return
    if d == M-1:
        print(arr)
        sum_v = sum(map(lambda x, y: x*y, arr, t))
        min_v = min(min_v, sum_v)
        return
    for j in range(i, N):
        arr[j] += 1
        f(i+1, d+1, sum_v + t[i])
        arr[j] -= 1

for tc in range(int(input())):
    # 심사대, 사람수
    N, M = map(int, input().split())
    t = sorted([int(input()) for _ in range(N)])
    arr = [0] * N
    min_v = 10000

    f(0, 0, 0)

    print(f'#{tc+1} {min_v}')
