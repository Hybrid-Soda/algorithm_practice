'''
    <힙 정렬>
    힙은 완전 이진 트리로서, 부모 노드의 값이 자식 노드의 값보다 항상 크거나 작은 특성을 가진다
    먼저 입력 배열을 힙으로 만든 다음, 최대 힙(Max Heap)에서 최댓값을 추출하여
    배열의 마지막 요소와 교환하는 과정을 반복하여 정렬
    힙 정렬은 평균 및 최악의 경우에도 시간 복잡도가 O(nlogn)으로 일정하며,
    제자리 정렬(In-place)이 가능한 특징을 가진다
'''

def heapify(arr, n, i):
    largest = i  # 최대값을 현재 노드로 설정
    left = 2*i + 1  # 왼쪽 자식 노드의 인덱스를 계산
    right = 2*i + 2  # 오른쪽 자식 노드의 인덱스를 계산

    # 왼쪽 자식 노드가 힙 범위 내에 있고, 현재 노드보다 크다면 최대값을 업데이트
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식 노드가 힙 범위 내에 있고, 현재 노드보다 크다면 최대값을 업데이트
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 최대값이 현재 노드가 아니라면 해당 노드와 최대값을 교환
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 교환 후, 교환된 자식 노드를 루트로 하는 서브트리에 대해 heapify를 재귀적으로 호출
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # 입력 배열을 최대 힙으로 만듦 (자식 노드가 있는 노드만 고려)
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    # 최대 힙에서 최댓값을 추출하여 정렬
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 최댓값을 배열의 마지막 요소와 교환
        heapify(arr, i, 0)  # 마지막 요소를 제외한 부분 배열에 대해 heapify를 호출