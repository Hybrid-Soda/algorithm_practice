# 19532 수학은 비대면강의입니다
# 연립방정식 a*x + b*y = c / d*x + e*y = f 를 푸는 문제
# number = -999 ~ 999

a, b, c, d, e, f = list(map(int, input().split()))

h = (a * e) - (b * d)
x = (((e * c) + (-b * f)) // h)
y = (((-d * c) + (a * f)) // h)

print(x, y)