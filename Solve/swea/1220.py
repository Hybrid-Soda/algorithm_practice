# 1220 Magnetic
# 교착 상태 카운트 : 다른 극의 자성체가 만나는 부분
# 자기장) 위 : N극 / 아래 : S극
# 자성체) 1 : N극 / 2 : S극

import sys
sys.stdin = open("input.txt")

for tc in range(10):
    N = int(input())
    # 테이블 및 스택의 위쪽이 N극 (1) / 아래쪽이 S극 (2)
    table = [list(map(int, input().split())) for _ in range(N)]
    deadlock = 0

    for i in range(N):
        stack = []
        for j in range(N-1,-1,-1):
            temp = table[j][i]
            # 스택에 원소가 없으면
            if not stack:
                # 자성체가 2(S극)이라면 스택에 추가
                if temp == 2:
                    stack.append(temp)
            # 스택에 원소가 있으면
            else:
                # 자성체가 1(N극)일때 스택에 남아있는 숫자가 2(S극)라면 교착 상태
                if temp == 1 and stack[-1] == 2:
                    stack.append(temp)
                    deadlock += 1
                # 자성체가 2(S극)일때 스택에 남아있는 숫자가 1(N극)이라면 스택에 추가만 함
                elif temp == 2 and stack[-1] == 1:
                    stack.append(temp)

    print(f'#{tc+1} {deadlock}')
