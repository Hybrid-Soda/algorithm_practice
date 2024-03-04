# 1744 수묶기

import sys 
sys.stdin = open('input.txt') 

N = int(input())
max_v = 0
num = sorted([int(input()) for _ in range(N)])

if N != 1:
    for i in range(0, N-1, 2):
        if num[i] * num[i+1] == 1:

        elif num[i] * num[i+1] > 0:
            max_v += num[i] * num[i+1]
        elif num[i] * num[i+1] < 0:
            max_v += num[i] + num[i+1]
        elif num[i] > 0 or num[i+1] > 0:
            max_v += num[i] + num[i+1]
    print(max_v)
else:
    print(*num)