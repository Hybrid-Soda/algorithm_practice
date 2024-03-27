import sys
sys.stdin = open('input.txt')

# N번째 수를 출력 / 666 - 1666 - 2666 - ... - 6660 - ...
# 완전 탐색 : 666이 3개 이상 나오는 수를 체크하며 카운트

N = int(input())
num = 665

while N > 0:
    num += 1
    if '666' in str(num):
        N -= 1
    
print(num)