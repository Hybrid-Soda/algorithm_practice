# 세탁소 사장 동혁
# 거스름돈 : 쿼터($0.25) / 다임($0.10) / 니켈($0.05) / 페니($0.01)
# 의 개수를 구하는 프로그램 작성
# 거스름돈 <= 5.00
# 동전의 개수 최소 / 센트 = $0.01

T = int(input())

for tc in range(T):
    C = int(input())
    quo_25, rem = divmod(C, 25)
    quo_10, rem = divmod(rem, 10)
    quo_5, rem = divmod(rem, 5)
    quo_1, rem = divmod(rem, 1)
    print(quo_25, quo_10, quo_5, quo_1)
