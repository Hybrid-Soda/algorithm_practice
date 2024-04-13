# 11729 하노이탑 이동 순서

import sys
sys.stdin = open('input.txt')

n = int(input())
rod = [[i for i in range(n, 0, -1)], [], []]

def move():
    