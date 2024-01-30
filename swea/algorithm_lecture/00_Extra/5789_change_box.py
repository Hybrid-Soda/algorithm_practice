# 5789 현주의 상자 바꾸기
# N : 상자의 개수 / 각 상자에는 숫자를 새길 수 있는데 처음에는 모두 0
# Q : 일정 범위의 연속한 상자를 동일한 숫자로 변경하는 횟수
# L번 상자부터 R번 상자까지의 값을 i로 변경

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, Q = map(int, input().split())
    change_box = [list(map(int, input().split())) for _ in range(Q)]
    box_list = [0] * N
    i = 1

    for work in change_box:
        L = work[0]
        R = work[1]
        for num in range(L-1, R):
            box_list[num] = i
        i += 1

    print(f'#{tc+1}', *box_list)
