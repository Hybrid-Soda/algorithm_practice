from sys import stdin
stdin = open('input.txt')

# 1427 소트인사이드
# N의 각 자리의 숫자를 정렬

print(''.join(list(map(str, sorted(list(input()), reverse=True)))))