'''
    <퀵 정렬>
    배열에서 피벗(pivot)을 선택하고,
    피벗을 기준으로 작은 요소들과 큰 요소들을 분할한 뒤
    각 부분 배열에 대해 재귀적으로 정렬하는 방식
'''

# 재귀 방식
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # 배열의 첫번째를 피벗으로 선택
    left = [x for x in arr[1:] if x <= pivot]  # 피벗보다 작거나 같은 요소
    right = [x for x in arr if x > pivot]  # 피벗보다 큰 요소
    
    # 각 부분 배열을 재귀적으로 정렬하고 합친다
    return quick_sort(left) + [pivot] + quick_sort(right)


# 스택 방식 - 함수 호출의 오버헤드를 줄이고, 메모리 사용량을 줄일 수 있다
def quick_sort(arr, low, high):
    stack = [(low, high)]  # 기본 범위
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition(arr, low, high)
            # 피벗을 기준으로 분할된 부분 배열을 스택에 추가
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

def partition(arr, low, high):
    # 배열의 마지막을 피벗으로 선택
    pivot = arr[high]
    i = low - 1

    # 피벗을 기준으로 작은 요소들을 피벗 왼쪽으로 옮긴다
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    # 피벗을 올바른 위치로 이동 (i-인덱스까지 피벗보다 작은 요소)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    # 피벗 인덱스 반환
    return i + 1
