'''
    <삽입 정렬>
    배열을 정렬된 부분과 정렬되지 않은 부분으로 나누고,
    정렬되지 않은 부분의 원소를 정렬된 부분에 삽입하여 정렬하는 방식
'''

def insertion_sort(arr):
    n = len(arr)

    # 배열의 두 번째 요소부터 시작
    for i in range(1, n):
        # 현재 요소를 key로 설정
        key = arr[i]
        # key의 바로 왼쪽 요소부터 시작
        j = i - 1

        # key보다 큰 값이 나올 때까지 정렬된 부분을 오른쪽으로 이동
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # key를 적절한 위치에 삽입
        arr[j + 1] = key