'''
    <버블 정렬>
    인접한 두 요소를 비교하여 순서를 바꿔가며 정렬을 수행
'''

# 작은 요소부터 정렬
def bubble_sort(arr):
    n = len(arr)
    # 배열의 길이만큼 반복
    for i in range(n):
        # 각 반복에서 가장 작은 요소가 배열의 왼쪽 끝으로 이동하므로, 정렬된 부분 제외한 범위 설정
        for j in range(n-1, i, -1):
            # 인접한 두 요소 비교 후 순서 변경
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

# 큰 요소부터 오름차순 정렬
def bubble_sort_asc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 큰 요소부터 내림차순 정렬
def bubble_sort_desc(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]