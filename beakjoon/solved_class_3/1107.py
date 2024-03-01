# 1107 리모컨

import sys
sys.stdin = open("input.txt")

N, M = list(int(input())), int(input())
broken = list(map(int, input().split()))
now = [1,0,0]

# 버튼을 누르지 않아도 되는 경우
if now:
    pass
# 버튼을 눌러야 하는 경우
else:
    for n in N:
        for i in range(10):
            if i not in broken: