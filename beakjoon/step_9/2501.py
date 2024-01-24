# 2501 약수 구하기
# case 1 : K번째 약수가 존재
# case 1-1 : K번째 약수가 N/2 미만
# case 1-1 : K번째 약수가 N/2
# case 1-2 : K번째 약수가 N
# case 2 : K번째 약수가 존재 x

N, K = map(int, input().split())


def count(N, ans, num, K):
    if N % num == 0:
        K -= 1
        ans = num
    return K, ans


num = 1
ans = 0
while K > 0:
    if num < N//2 + 1:
        K, ans = count(N, ans, num, K)
    elif num == N//2 + 1:
        K, ans = count(N, ans, num, K)
        num = N-1
    elif N//2 + 1 < num and num <= N:
        K, ans = count(N, ans, num, K)
    elif num > N:
        ans = 0
        break

    num += 1

print(ans)
