# 11727 2xn 타일링 2
# 부분 -> 전체 : DP

N = int(input())
DP = [0, 1, 3] + [0] * 998

if N >= 3:
    for i in range(3, N+1):
        DP[i] = 2*DP[i-2] + DP[i-1]

print(DP[N] % 10007)