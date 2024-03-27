# 1824 혁진이의 프로그램 검증

import sys
import random
sys.stdin = open("input.txt")

#    우  하  좌  상
di = (0, 1, 0, -1)
dj = (1, 0, -1, 0)

for tc in range(int(input())):
    R, C = map(int, input().split())
    char = [input() for _ in range(R)]
    i, j, k, mem, end = 0, 0, 0, 0, 'NO'
    can_end, cnt = False, 0
    
    for row in char:
        if '@' in row:
            can_end = True; break

    while can_end:
        n = char[i][j]
        if n == '.': pass
        elif n == '>': k = 0
        elif n == 'v': k = 1
        elif n == '<': k = 2
        elif n == '^': k = 3
        elif n == '?': k = random.randint(0, 3)
        elif n.isdecimal(): mem = int(n)
        elif n == '_':
            cnt += 1
            if cnt > 50: break
            if mem == 0: k = 0
            else: k = 2
        elif n == '|':
            cnt += 1
            if cnt > 50: break
            if mem == 0: k = 1
            else: k = 3
        elif n == '+':
            mem += 1
            if mem > 15: mem = 0
        elif n == '-':
            mem -= 1
            if mem < 0: mem = 15
        elif n == '@': end = 'YES'; break

        i += di[k]; j += dj[k]
        if i < 0: i = R - 1
        elif i >= R: i = 0
        elif j < 0: j = C - 1
        elif j >= C: j = 0

    print(f'#{tc+1} {end}')