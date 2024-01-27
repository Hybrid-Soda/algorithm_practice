import sys
sys.stdin = open('input.txt')

# 25305 커트라인
# N 중 k번째 높은 숫자를 구하라

N, k = map(int, input().split())
arr = list(map(int, input().split()))
print(sorted(arr)[-k])