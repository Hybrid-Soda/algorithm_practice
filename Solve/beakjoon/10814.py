import sys
sys.stdin = open('input.txt')

# 10814 나이순 정렬
# 1. 나이 오른차순 / 2. 이름 먼저 가입한 사람 순
# 이름 먼저 가입한 사람 순 keep하는 방법 -> 그냥 버블정렬 해야할듯

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
	age, name = sys.stdin.readline().split()
	arr.append([int(age), name])

arr.sort(key= lambda x: x[0])

for i in arr:
	print(i[0],i[1])