import sys
sys.stdin = open('input.txt')

# N번째 수를 출력 / 666 - 1666 - 2666 - ... - 6660 - ...
print(str(int(input()) - 1) + '666')
