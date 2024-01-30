# 9386 연속한 1의 개수
# 수열에서 연속한 1의 개수 중 최대값을 출력

import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N = int(input())
    # 수열
    sequence = list(input())
    # 답
    ans = 1
    # 부분별 연속한 개수 세기위한 변수
    temp = 1

    # 수열 길이 -1 순회
    for i in range(len(sequence)-1):
        # 만약 현재 숫자와 다음 숫자가 1로 같으면 연속수 카운트
        if sequence[i] == sequence[i+1] == '1':
            temp += 1
            # 답과 임시 변수 비교 후 최댓값을 답으로 설정
            ans = max(ans, temp)
        # 아니면 초기화
        else:
            temp = 1
    # 1이 수열에 없으면 답은 0
    if '1' not in sequence:
        ans = 0

    print(f'#{tc+1} {ans}')