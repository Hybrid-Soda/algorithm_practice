'''
    <카운팅 정렬>
    정수 배열의 요소들이 특정 범위 내에 있을 때에만 사용 가능
    범위가 크지 않을 때에 가장 빠른 정렬 알고리즘 중 하나
    각 요소의 출현 빈도를 계산하여 정렬
'''

def counting_sort(arr):
    # 배열의 최댓값
    max_val = max(arr)
    
    # 배열의 최댓값에 1을 더한 크기의 카운트 배열 생성
    count = [0] * (max_val + 1)
    
    # 각 요소의 출현 빈도 카운트
    for num in arr:
        count[num] += 1
    
    # 누적 합 계산
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # 정렬된 배열을 저장할 배열 생성
    sorted_arr = [0] * len(arr)
    
    # 카운트 배열을 이용하여 정렬
    for num in reversed(arr):
        sorted_arr[count[num] - 1] = num
        count[num] -= 1
    
    # 정렬된 배열을 반환
    return sorted_arr
