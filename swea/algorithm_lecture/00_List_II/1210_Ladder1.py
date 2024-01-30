# 1210 Ladder1
# 100 x 100 크기의 2차원 배열로 주어진 사다리를 타서
# 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성 / 도착점은 2로 표현
# 출발점을 x좌표로 출력

import sys
sys.stdin = open("input.txt")

for i in range(10):
    case_num = int(input())
    # 양 끝에 벽을 세워줌
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
    # 도착점 위치로 시작하는 현 위치
    col, row = ladder[-1].index(2), 99

    # 역사다리타기 시작 : row 인덱스가 0이 되면 loop 종료
    while row != 0:
        # 왼쪽에 사다리가 있다면 왼쪽으로 진행
        if ladder[row][col - 1] == 1:
            while ladder[row][col - 1] == 1:
                col -= 1
            row -= 1
        # 오른쪽에 사다리가 있다면 오른쪽으로 진행
        elif ladder[row][col + 1] == 1:
            while ladder[row][col + 1] == 1:
                col += 1
            row -= 1
        # 현재 열의 좌우에 사다리가 없다면 위로 진행
        else:
            row -= 1

    print(f'#{case_num} {col-1}')
