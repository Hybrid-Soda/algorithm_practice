# [HSAT 6회 정기 코딩 인증평가 기출] 염기서열 커버

import sys
sys.stdin = open("input.txt")

def gen_super_gene(i):
    print(bin(i))


n, m = map(int, input().split())
gene = [list(input()) for _ in range(n)]
super_gene = [None for _ in range(1<<n)]

for i in range(1, 1<<n):
    gen_super_gene(i)