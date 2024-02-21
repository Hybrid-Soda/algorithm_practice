# 1891 / 사분면 / 골드4

import sys
sys.stdin = open("input.txt")

# 주어진 번호로 인덱스 추적
def get_coor(n, idx, row, col):
    # 탈출 조건: 분할 완료 시
    if n == 0: return row, col
    # 반복 분할
    if num[idx] == '1': return get_coor(n//2, idx+1, row, col + n)
    elif num[idx] == '2': return get_coor(n//2, idx+1, row, col)
    elif num[idx] == '3': return get_coor(n//2, idx+1, row + n, col)
    elif num[idx] == '4': return get_coor(n//2, idx+1, row + n, col + n)

# 사분면 번호 제작
def make_num(n, i, j, num_v):
    print('hi')
    # 탈출 조건 : 자릿수가 채워질 경우
    if len(num_v) == d: print(num_v); return num_v
    # 반복 분할
    if (i <= row <= i + n//2) and (j + n//2 < col < j + n):
        return make_num(n//2, i, j + n//2, num_v + '1')
    elif (i <= row <= i + n//2) and (j <= col <= j + n//2):
        return make_num(n//2, i, j, num_v + '2')
    elif (i + n//2 < row < i + n) and (j <= col <= j + n//2):
        return make_num(n//2, i + n//2, j, num_v + '3')
    elif (i + n//2 < row < i + n) and (j + n//2 < col < j + n):
        return make_num(n//2, i + n//2, j + n//2, num_v + '4')


d, num = input().split(); d = int(d)
x, y = map(int, input().split())

row, col = get_coor(2**d//2, 0, 0, 0)
row += x; col += y
print(make_num(2**d, 0, 0, ''))




# 메모리 초과
'''
def div_conq(n, i, j, quad):
    if len(quad) == d:
        arr[i][j] = quad
        return
    div_conq(n//2, i, j + n, quad + "1")
    div_conq(n//2, i, j, quad + "2")
    div_conq(n//2, i + n, j, quad + "3")
    div_conq(n//2, i + n, j + n, quad + "4")

d, num = map(int, input().split())
x, y = map(int, input().split())
N = int(4 ** (d / 2))
arr = [[0] * N for _ in range(N)]

div_conq(N//2, 0, 0, '')

for i in range(N):
    for j in range(N):
        if arr[i][j] == str(num):
            row, col = i, j
            break
try:
    print(arr[row-y][col+x])
except:
    print(-1)
'''