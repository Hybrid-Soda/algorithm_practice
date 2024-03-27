'''
    <합병 정렬>
    재귀적으로 배열을 분할하고 이를 다시 합치면서 정렬하는 방식
    합병 정렬은 평균 시간 복잡도가 O(nlogn)으로 안정적이며,
    대규모 데이터에도 효과적으로 동작한다
'''

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # 배열을 반으로 나눔
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # 왼쪽 반과 오른쪽 반을 재귀적으로 합병 정렬
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # 정렬된 두 배열을 합병하여 반환
    return merge(left_half, right_half)


def merge(left_half, right_half):
    merged_arr = []
    l, r = 0, 0

    # 왼쪽과 오른쪽 합병
    while l < len(left_half) and r < len(right_half):
        if left_half[l] < right_half[r]:
            merged_arr.append(left_half[l])
            l += 1
        else:
            merged_arr.append(right_half[r])
            r += 1

    # 남은 요소들을 합병
    merged_arr.extend(left_half[l:])
    merged_arr.extend(right_half[r:])

    return merged_arr