# 1217 거듭제곱
# N의 M 거듭제곱 값을 구하는 프로그램을 재귀호출을 이용하여 구현

import sys
sys.stdin = open("input.txt")

# 재귀 호출을 통해 거듭제곱을 구하는 함수
def power(base, exponent, count):
    # 카운트가 목표 거듭제곱에 도달하면 밑만 곱함
    if count == exponent:
        return base
    # 카운트가 목표 거듭베곱에 못미치면 재귀 호출
    else:
        count += 1
        return base * power(base, exponent, count)


for i in range(10):
    test_case = input()
    base, exponent = map(int, input().split())
    count = 1

    # 함수 호출 및 결과 출력
    print(f'#{test_case} {power(base, exponent, count)}')
