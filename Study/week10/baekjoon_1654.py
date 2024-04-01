# 1654 랜선 자르기

import sys
sys.stdin = open('input.txt')

def valid(length, cables):
    cnt = 0
    for cable in cables:
        while cable >= length:
            cable -= length
            cnt += 1
    return cnt

def search(start, end, cables):
    ans = 0
    while start < end:
        print(start, end)
        mid = (start + end) // 2
        if valid(mid, cables) >= N:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    return ans

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

print(search(0, max(cables), cables))