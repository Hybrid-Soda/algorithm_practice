# 20529 가장 가까운 세 사람의 심리적 거리

import sys
sys.stdin = open("input.txt")
from itertools import combinations

for _ in range(int(input())):
    N, mbti = int(input()), input().split()
    ans = 100000

    if N > 32: print(0)  # 비둘기 집 원리
    else:
        for part in set(combinations(mbti, 3)):
            cnt = 0
            for i in map(set, zip(*part)):
                cnt += 2 if len(i) == 2 else 0
            ans = min(ans, cnt)
        
        print(ans)
