# 5086 배수와 약수

# 두 수가 주어졌을 때, 다음 3가지 중 어떤 관계인지 구하는 프로그램을 작성하시오.
# 1. 첫 번째 숫자가 두 번째 숫자의 약수이다.
# 2. 첫 번째 숫자가 두 번째 숫자의 배수이다.
# 3. 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다.
# 입력 : 여러 테스트 케이스 / 각 테스트 케이스는 10,000이 넘지않는 두 자연수로 이루어짐
# 마지막 줄에는 0이 2개 주어진다. 두 수가 같은 경우는 없다.
# 출력 : 첫 번째 숫자가 두 번째 숫자의 약수 > factor, 배수 > multiple, 둘 다 X > neither 출력

while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break

    if (num1 % num2) == 0:
        print('multiple')
    else:
        if (num2 % num1) == 0:
            print("factor")
        else:
            print("neither")
