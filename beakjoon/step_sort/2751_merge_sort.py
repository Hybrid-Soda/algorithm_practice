from sys import stdin
stdin = open('input.txt')

# 2751 수 정렬하기 2
# N개의 수 어름차순 정렬
# 1 <= N <= 1,000,000
# 합병 정렬 이용

N = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(N)]


def merge_sort(arr):
    # 만약 배열의 원소가 여러 개라면 조건문 실행
    if len(arr) > 1:
        # 배열의 중간을 기준으로 분할
        mid = len(arr) // 2
        LHS = arr[:mid]
        RHS = arr[mid:]

        # 배열의 원소가 한개가 될 때까지 분할 (재귀함수)
        merge_sort(LHS)
        merge_sort(RHS)

        i = j = k = 0

        # 두 개의 부분 배열을 합병
        # 배열의 원소가 한개가 되면서 비로소 도달
        # 한쪽 배열을 모두 순회하게 되면 중단
        while i < len(LHS) and j < len(RHS):
            # 왼쪽 값이 오른쪽 값보다 작다면
            if LHS[i] < RHS[j]:
                # k번째 원소는 왼쪽 값
                arr[k] = LHS[i]
                # 왼쪽 인덱스를 증가시키며 진행
                i += 1
            # 오른쪽 값이 왼쪽 값보다 작다면
            else:
                # k번째 원소는 오른쪽 값
                arr[k] = RHS[j]
                # 오른쪽 인덱스를 증가시키며 진행
                j += 1
            # 부분 배열의 다음 인덱스의 값을 결정짓기 위해 증가
            k += 1

        # 남은 요소들을 복사 (이미 남은 요소들은 정렬되어 있음)
        while i < len(LHS):
            arr[k] = LHS[i]
            i += 1
            k += 1

        while j < len(RHS):
            arr[k] = RHS[j]
            j += 1
            k += 1
    
    return arr


for i in merge_sort(arr):
    print(i)