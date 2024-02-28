# 5430 AC

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    p, n = input().replace('RR', ''), int(input())
    arr = input().strip('[]').split(',')
    if arr == ['']: arr = []

    for c in p:
        if c == 'R':  arr.reverse()
        elif c == 'D':
            try:
                arr.pop(0)
            except IndexError:
                print('error'); break
    else:
        print(f"[{','.join(arr)}]")