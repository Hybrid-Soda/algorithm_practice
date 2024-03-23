'''
    <보이어-무어(Boyer-Moore) 알고리즘>
    문자열 검색에서 가장 효율적인 알고리즘 중 하나
    핵심 : 대부분의 상황에서 검색하려는 패턴의 모든 문자를 비교하지 않아도 됨
    주요 전략 : 나쁜 문자 규칙(Bad Character Rule), 좋은 접미사 규칙(Good Suffix Rule)
'''

# 나쁜 문자 규칙
def boyer_moore_search(text, pattern):
    # 텍스트와 패턴의 길이
    m, n = len(pattern), len(text)

    # 나쁜 문자 규칙을 위한 이동 테이블 생성
    shift = {char: index for index, char in enumerate(pattern)}

    cnt = s = 0  # text에 대한 pattern의 현재 시작 위치
    while s <= n - m:
        # 패턴의 마지막 문자부터 비교 시작
        j = m - 1

        # 패턴의 마지막 문자와 일치하는 문자를 찾을 때까지 왼쪽으로 이동
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # 패턴이 일치하는 경우 위치 반환
        if j < 0:
            cnt += 1
            print(f"Pattern occurs at shift = {s}")
            s += (m - shift[text[s + m]] if s + m < n else 1)
        else:
            # 나쁜 문자 규칙에 따라 s를 조정
            char_shift = shift.get(text[s + j])
            s += max(1, j - char_shift)

    return cnt