import sys
sys.stdin = open('input.txt')
# 1018 체스판 다시 칠하기
# M * N 크기의 보드 -> 8 * 8 크기의 체스판을 골라냄
# 최소한으로 색칠해야 함
# 최대한 교대로 칠해져 있는 부분을 찾고 그 쪽 부분이 많게 잘라야 함
# 체크무늬 많은 부분 어떻게 찾나?
# 1. 일일이 찾기 처음부분부터 진행하면서 8*8로 자른 후 개수 세기 -> 반복 후 제일 적은 값 도출
# 1-1. 일일히 찾는 알고리즘 -> B와 W가 교대로 있는지 확인
# 1-2. 왼쪽 위가 B일 때와 W일 때 둘다 체크

# 입력 : 체스판의 크기와 각 칸의 색을 입력 받음
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
ans = 64

# 탐색 : 원래 보드를 순회하며 슬라이스해서 8x8 보드 생성
for row in range(N-7):
    for col in range(M-7):
        '''
        밑의 for 문을 (row, row+8) / (col, col+8) 범위에서 반복시키고
        subarray는 제작 안해도 됨

        그리고 for문을 두번 줄 필요 없이 if문에서 합쳐도 됨
        왜냐하면 for~ range(8)이 겹치므로 합칠 방법이 있으면 합칠 수 있음

        if (x+y) %2 ==0:
            if data[x][y]!='W':
                w_count+=1
            if data[x][y]!='B':
                b_count+=1
        else:
            if data[x][y]!='B':
                w_count+=1
            if data[x][y]!='W':
                b_count+=1
        '''
        subarray = [i[col:col+8] for i in board[row:row+8]]
        b_count = 0
        w_count = 0
        # 계산 : 8x8 크기로 자른 보드에 새로 칠해야 하는 부분 계산
        # B가 왼쪽 위인 경우 기준
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0 and subarray[i][j] != 'B':
                    b_count += 1
                elif (i+j)%2 == 1 and subarray[i][j] != 'W':
                    b_count += 1
        # W가 왼쪽 위인 경우 기준
        for i in range(8):
            for j in range(8):
                if (i+j)%2 == 0 and subarray[i][j] != 'W':
                    w_count += 1
                elif (i+j)%2 == 1 and subarray[i][j] != 'B':
                    w_count += 1
        count = min(b_count, w_count)
        # 갱신 : 이전 개수보다 칠해야 하는 정사각형이 적으면 저장
        if count < ans:
            ans = count
        '''
        ans = min(ans, count) 로 대체 가능
        '''

# 칠해야 하는 정사각형 개수의 최소값 출력
print(ans)
