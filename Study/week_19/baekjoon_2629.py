# 2629 양팔저울

import sys
sys.stdin = open('input.txt')

N = int(input())
weight_N = list(map(int, input().split()))

M = int(input())
weight_M = list(map(int, input().split()))

for w in weight_M:
    # 추의 무게와 같은 무게일때
    if w in weight_N:
        break
    # 추끼리의 합,차로 도출되는 무게일때
    total_weight = 0
    for i in weight_N:
        total_weight += i
        if i == w or w:
            break
    # 두 추의 무게 사이에 각각 1의 차이로 있을때
    
    # 추를 두 그룹으로 나눈다
    