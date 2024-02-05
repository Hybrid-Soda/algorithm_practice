# 4865 글자수
# 문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고
# 그중 가장 많은 글자의 개수 출력
# 파이썬의 경우 딕셔너리 사용 가능

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    # str1 딕셔너리 제작
    str1 = {}
    for text in input():
        str1[text] = 0

    # str2 문자열로 입력
    str2 = input()

    # str2의 글자 순회
    for text in str2:
        # str2의 각 글자가 str1에 있다면 카운트
        if text in str1.keys():
            str1[text] += 1

    # str1 딕셔너리에서 카운트한 숫자 중 최대값 출력
    print(f'#{tc+1} {max(str1.values())}')