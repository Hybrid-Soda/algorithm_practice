# 2470 두 용액

import sys
sys.stdin = open('input.txt')

def comb(arr, i):
    if len(arr) == 2:
        global min_v
        min_v = min(min_v, abs(sum(arr)))
        if min_v == abs(sum(arr)):
            global num1; global num2
            num1 = min(arr)
            num2 = max(arr)
        return
    elif i < len(feat):
        comb(arr, i+1)
        comb(arr+[feat[i]], i+1)

N, min_v = int(input()), 1e+10
feat = list(map(int, input().split()))
num1, num2 = 0, 0
comb([], 0)
print(num1, num2)