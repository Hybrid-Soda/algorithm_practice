def comb(arr):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N + 1):
        if arr:
            if arr[-1] <= i:
                comb(arr + [i])
        else:
            comb(arr + [i])


N, M = map(int, input().split())
comb([])
