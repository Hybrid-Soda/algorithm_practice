'''
    파이썬 진수 변환 : 2진수 -> 10진수
'''
str2 = '1010'

# 1. 내장함수 int() 사용
num10 = int(str2, 2)
print(num10)

# 2. 수동 변환
num10 = 0
for i, bit in enumerate(reversed(str2)):
    num10 += int(bit) * 2**i
print(num10)

# 3. eval() 함수 사용
num10 = eval('0b' + str2)
print(num10)

# 4. 비트 연산 사용
num10 = 0
for bit in str2:
    # decimal_number의 모든 비트를 왼쪽으로 한 자리 이동시키며 'or' 연산자로 계산
    num10 = (num10 << 1) | int(bit)
print(num10)


'''
    파이썬 진수 변환 : 10진수 -> 2진수
'''
num10 = 10

# 1. 내장함수 bin() 사용
str2 = bin(num10)
print(str2[2:])

# 2. 내장함수 format() 사용
str2 = format(num10, 'b')
print(str2)

# 3. f-string 사용
str2 = f"{num10:b}"  # f"{num10:06b}" -> 6자리 나타냄
print(str2)

# 4. 수동 변환
str2 = ''
while num10 > 0:
    str2 = str(num10 % 2) + str2
    num10 //= 2
print(str2)


'''
    파이썬 진수 변환 : 16진수 -> 10진수
'''
str16 = 'a'

# 1. 내장함수 int() 사용
num10 = int(str16, 16)
print(num10)

# 2. 수동 변환
num10 = 0
for i, digit in enumerate(reversed(str16)):
    num10 += int(digit, 16) * 16**i
print(num10)

# 3. eval() 함수 사용
num10 = eval('0x' + str16)
print(num10)


'''
    파이썬 진수 변환 : 10진수 -> 16진수
'''
num10 = 10

# 1. 내장함수 hex() 사용
str16 = hex(num10)
print(str16[2:])

# 2. 내장함수 format() 사용
str16 = format(num10, 'x')
print(str16)

# 3. f-string 사용
str16 = f"{num10:x}"
print(str16)