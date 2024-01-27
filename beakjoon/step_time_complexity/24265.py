# 24265 알고리즘 수업 - 알고리즘의 수행 시간 4
# def MenOfPassion(A[], n):
#     sum = 0
#     for i in range(n-1):
#         for j in range(i, n):
#             sum += A[i] * A[j]
#     return sum
# 2 3 4 5 6 7 / 3 4 5 6 7 / 4 5 6 7 / 5 6 7 / 6 7 / 7 -> 1부터 6까지의 합
# n(n-1)/2

n = int(input())
print(f'{int(n*(n-1)/2)}\n2')
