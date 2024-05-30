# 1052 물병

import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
ans = float('inf')
quotient = 0
remainder = N

while remainder >= K:
    remainder >>= 1
    quotient += 1

print(ans if ans != float('inf') else -1)