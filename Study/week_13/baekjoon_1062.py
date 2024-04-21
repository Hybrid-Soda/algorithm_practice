# 1062 가르침

import sys
sys.stdin = open('input.txt')

def change(word):
    word = set(word)
    for char in ['a', 'n', 't', 'i', 'c']:
        word.remove(char)
    return ''.join(word)

N, K = map(int, input().split())
words = [change(input()) for _ in range(N)]

if K < 5: exit(print(0))


print(words)