# 10773 제로

import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline
stack = []

for _ in range(int(input())):
    num = int(input())
    
    if num != 0:
        stack.append(num)
    else:
        stack.pop()
    
print(sum(stack))