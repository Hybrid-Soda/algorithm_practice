import sys
sys.stdin = open('input.txt')

# 2587 대표값2
# 평균과 중앙값 구하기

arr = [int(input()) for i in range(5)]
print(sum(arr)//5)
print(sorted(arr)[2])