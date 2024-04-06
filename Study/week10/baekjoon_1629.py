# 1629 곱셈

# A를 B번 곱한 수 (C로 나누어줌)
A, B, C = map(int, input().split())
def power(A, B, C):
    if B == 1: return A % C
    elif B % 2: return A * power(A, B-1, C) % C
    else: return power(A, B//2, C)**2 % C
print(power(A, B, C))