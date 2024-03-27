from sys import stdin
stdin = open('input.txt')

# 11650 좌표 정렬하기
# 점 N개 / x좌표 증가 순 -> y좌표 증가 순 정렬

N = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for i in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
for i in arr:
    print(*i)

'''
문자열로 입력을 받고 정렬하고 있기 때문에
의도한 대로 작동하지 않을 수 있습니다.
좌표를 비교할 때는 숫자로 비교해야 합니다.
입력을 숫자로 변환하고, x[0]을 기준으로 정렬하고 x[1]을 기준으로 정렬
'''
