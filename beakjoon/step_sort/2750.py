import sys
sys.stdin = open('input.txt')

# 2750 수 정렬하기
# N개의 수 오름차순 정렬
# 버블 정렬
# 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
# 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬된다
# 교환하며 자리를 이동하는 모습이 물 위에 올라오는 거품 같다고 하여 버블 정렬

N = int(input())
arr = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(0, N-i-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
            
for i in arr:
    print(i)