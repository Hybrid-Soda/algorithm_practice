# 1213 String
# 주어지는 문장에서 특정한 문자열의 개수를 반환

import sys
sys.stdin = open("input.txt", encoding="utf-8")

for tc in range(10):
    test_case = input()
    find_str = input()    # 찾을 문자열
    sentence = input()    # 검색할 문장
    # 사실 `ans = sentence.count(find_str)` 한 줄로 끝낼 수는 있음
    ans = 0

    # 검색할 문장 길이만큼 순회
    for i in range(len(sentence)):

        # 찾을 문자열의 첫 글자와 문장의 글자가 같다면 비교 시작
        if sentence[i] == find_str[0] and i != len(sentence)-1:
            j = 1

            # 비교글자가 같을 때만 진행
            while sentence[i+j] == find_str[j]:
                j += 1

                # 끝까지 진행되었다면 카운트
                if j == len(find_str):
                    ans += 1
                    break
    
    print(f'#{test_case} {ans}')