# 1193 분수찾기
# 행렬 응용 / 사선으로 진행
# 각 레이어 분수의 분모 분자의 합은 레이어 + 1
# ex) 5번 레이어의 분모 분자 합은 6

X = int(input())
i = 0

while X > i:
    X -= i
    i += 1

if i % 2 == 0:
    print(f'{X}/{i-X+1}')
else:
    print(f'{i-X+1}/{X}')
