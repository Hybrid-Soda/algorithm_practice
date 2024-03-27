# 1541 잃어버린 괄호
# 괄호를 적절히 쳐서 식의 값을 최소로 만들기
# 마이너스 뒤에 괄호 (다음 마이너스 나오기 전까지 혹은 식이 끝나기 전까지)

import sys
sys.stdin = open("input.txt")

equ = list(map(lambda x: sum(map(int, x.split('+'))), input().split('-')))
ans = equ[0]
for num in equ[1:]:
    ans -= num

print(ans)