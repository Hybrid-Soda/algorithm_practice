# 2382 미생물 격리
# 목표 : M시간 후 남아있는 미생물 수의 총 합 구하기

import sys
sys.stdin = open("input.txt")

class Micro:
    def __init__(self, row, col, cnt, dir):
        self.row = row
        self.col = col
        self.cnt = cnt
        self.dir = dir
        self.pos = (row//N)*N + col

    def change_dir(self):
        self.cnt //= 2
        if self.dir in [1, 3]: self.dir += 1
        else: self.dir -= 1

    def merge(self, other):
        if self.cnt > other.cnt:
            self.cnt += other.cnt
            other.cnt = 0
        else:
            other.cnt += self.cnt
            self.cnt = 0

def task(info):
    for micro in info:
        micro.row += dr[micro.dir]
        micro.col += dc[micro.dir]
        micro.pos = (micro.row//N)*N + micro.col

        if not (0 < micro.row < N-1 and 0 < micro.col < N-1):
            micro.change_dir()

            if not micro.cnt:
                info.remove(micro)

    info.sort(key=lambda x: (x.pos, x.cnt))

    idx = 0
    while idx < len(info)-1:
        if info[idx].pos == info[idx+1].pos:
            info[idx+1].cnt += info[idx].cnt
            info.remove(info[idx])
            idx -= 1
        idx += 1

dr = (0, -1, 1, 0, 0)
dc = (0, 0, 0, -1, 1)

for tc in range(int(input())):
    N, M, K = map(int, input().split())
    info = [Micro(*map(int, input().split())) for _ in range(K)]
    for time in range(M): task(info)
    print(f"#{tc+1}", sum(micro.cnt for micro in info))