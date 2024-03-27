# 1931 회의실 배정
# 최대 사용할 수 있는 회의의 최대 개수 출력

import sys
input = sys.stdin.readline
sys.stdin = open("input.txt")

meetings = [list(map(int, input().split())) for _ in range(int(input()))]
meetings.sort(key=lambda x: (x[1], x[0]))

cnt = 0
temp = 0

for start, end in meetings:
    if temp <= start:
        cnt += 1
        temp = end

print(cnt)