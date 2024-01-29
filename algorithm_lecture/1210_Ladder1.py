# 1210 Ladder1
# 100 x 100 크기의 2차원 배열로 주어진 사다리를 타서
# 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성 / 도착점은 2로 표현
# 출발점을 x좌표로 출력

import sys
sys.stdin = open("input.txt")

for i in range(1):
    case_num = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착점 위치로 시작하는 현 위치
    x, y = ladder[-1].index(2), 99
    
    # 역사다리타기 시작 : y인덱스가 0이 되면 loop 종료
    while y != 0:
        # 현재 열의 좌우에 사다리가 없다면 위로 진행
        if x > 0 and ladder[y][x + 1] == 0 and ladder[y][x - 1] == 0:
            y -= 1
        # 왼쪽에 사다리가 있다면 왼쪽으로 진행
        elif ladder[y][x - 1] == 1:
            while ladder[x - 1] == 1:
                x -= 1
            y -= 1
        # 오른쪽에 사다리가 있다면 오른쪽으로 진행
        else:
            while ladder[y][x + 1] == 1:
                x += 1
            y -= 1
    print(f'#{case_num} {x}')