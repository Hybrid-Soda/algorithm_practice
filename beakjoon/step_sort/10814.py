import sys
sys.stdin = open('input.txt')

# 10814 나이순 정렬
# 1. 나이 오른차순 / 2. 이름 먼저 가입한 사람 순
# 이름 먼저 가입한 사람 순 keep하는 방법 -> 그냥 버블정렬 해야할듯

N = int(input())
arr = [input().split() for _ in range(N)]

def asc(arr, N):
	for i in range(N-1, 0, -1):
		for j in range(i):
			if int(arr[j][0]) > int(arr[j+1][0]):
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr

print(asc(arr, N))