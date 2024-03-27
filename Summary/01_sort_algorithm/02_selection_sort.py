'''
    <선택 정렬>
    리스트에서 가장 작은(또는 가장 큰) 요소를 선택하여
    맨 앞(또는 맨 뒤)으로 이동시키는 정렬 알고리즘
'''

def selection_sort(arr):
    n = len(arr)

    # 배열의 길이만큼 반복
    for i in range(n):
        # 현재 인덱스를 가장 작은 원소로 설정
        min_index = i

        # 현재 인덱스 이후의 원소들 중에서 가장 작은 값을 찾는다
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # 가장 작은 값을 현재 인덱스와 교환
        arr[i], arr[min_index] = arr[min_index], arr[i]