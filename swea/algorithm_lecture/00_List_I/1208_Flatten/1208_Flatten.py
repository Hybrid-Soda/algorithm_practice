# 1208 Flatten

import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    # 덤프 횟수
    dump = int(input())
    # 박스가 쌓여있는 모습
    box = list(map(int, input().split()))
    # 덤프 횟수만큼 순회
    for i in range(dump):
        # 최대점에서 최소점에 박스를 옮김
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1
    
    # 순회가 끝난 후 최고점과 최저점의 높이차를 출력
    print(f'#{tc} {max(box)-min(box)}')
