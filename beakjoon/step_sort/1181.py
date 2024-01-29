import sys
sys.stdin = open('input.txt')

# 1181 단어 정렬
# N개의 단어 정렬
# 1. 길이가 짧은 것부터 / 2. 길이가 같으면 사전 순으로
# 중복된 단어는 하나만 남기고 제거

N = int(sys.stdin.readline())
word_arr = list(set([sys.stdin.readline().strip() for _ in range(N)]))
word_arr.sort()
word_arr.sort(key= len)

for word in word_arr:
    print(word)
