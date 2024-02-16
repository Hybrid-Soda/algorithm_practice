# 2304 창고 다각형
# 목표 : 가장 작은 창고 다각형의 면적 구하기
# 제일 큰 값을 기준으로 양 옆에 갈 수록 낮아지는 구조

import sys
sys.stdin = open('input.txt')

N = int(input())
column = sorted(tuple(map(int, input().split())) for _ in range(N))
idx, height = list(zip(*column))
print(height)

print(column)

# for col in column: