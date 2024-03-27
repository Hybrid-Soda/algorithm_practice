# 5430 AC

import sys
sys.stdin = open("input.txt")
from collections import deque
input = sys.stdin.readline

for tc in range(int(input())):
    p, n = input().replace('RR', ''), int(input())
    Q = deque(input().strip()[1:-1].split(','))
    rev = 0
    if '' in Q: Q.popleft()

    for c in p:
        if c == 'R': rev += 1
        elif c == 'D':
            try:
                if rev % 2 == 0: Q.popleft()
                else: Q.pop()
            except IndexError: print('error'); break
    else:
        if rev % 2 != 0: Q.reverse()
        print(f"[{','.join(Q)}]")