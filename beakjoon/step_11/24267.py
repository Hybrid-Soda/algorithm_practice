# 24266 알고리즘 수업 - 알고리즘의 수행 시간 5
# def MenOfPassion(A[], n):
#     sum = 0
#     for i in range(1, n-1):  # 1 ~ 5
#         for j in range(i+1, n):  # i+1 ~ 6
#             for k in range(j+1, n+1):  # j+1 ~ 7
#                 sum += A[i] * A[j] * A[k]
#     return sum
# 

n = int(input())
print(f'{(((n-2)*(n-1)*(2*n-3)+3*(n-1)*(n-2))//12)}\n3')

# 3 4 5 6 7 / 4 5 6 7 / 5 6 7 / 6 7 / 7 -> sum 1~5
# 4 5 6 7 / 5 6 7 / 6 7 / 7 -> sum 1~4
# 5 6 7 / 6 7 / 7 -> sum 1~3
# 6 7 / 7 -> sum 1~2
# 7 -> sum 1