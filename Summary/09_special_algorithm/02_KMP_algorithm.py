'''
    <KMP(Knuth-Morris-Pratt) 알고리즘>
    문자열 검색 알고리즘 중 하나로, 특정 문자열에서 부분 문자열을 찾는 데 사용
    핵심 : 불일치가 발생했을 때, 이전에 이미 일치했던 부분에 대한 정보를 활용하여 불필요한 비교를 최소화하는 것
    이를 위해 '부분 일치 테이블(Partial Match Table)' 또는 '파이(Pi) 테이블'이라고 불리는 배열을 미리 계산하여 사용
'''

# KMP 알고리즘을 사용하여 문자열에서 패턴의 발생 횟수를 찾는 함수
def KMP_search(string, pattern):
    # 부분 일치 테이블 초기화
    pi_table = [0] * len(pattern)

    # 부분 일치 테이블 생성
    for i in range(1, len(pattern)):
        # 이전 위치에서의 일치 길이를 기반으로 현재 위치의 일치 길이를 계산
        if pattern[pi_table[i-1]] == pattern[i]:
            pi_table[i] = pi_table[i-1] + 1

    cnt = 0  # 발견된 패턴의 횟수
    j = 0  # pattern의 현재 인덱스

    # 문자열을 순회하면서 패턴 매칭 검사
    for i in range(len(string)):
        # 현재 문자가 패턴의 문자와 일치하지 않을 때,
        # 부분 일치 테이블을 사용하여 j 인덱스를 조정
        while j > 0 and string[i] != pattern[j]:
            j = pi_table[j - 1]
        
        # 현재 문자가 패턴의 문자와 일치하면
        if string[i] == pattern[j]:
            # 패턴의 마지막 문자까지 모두 일치하는 경우
            if j == len(pattern) - 1:
                cnt += 1  # 발견된 횟수 증가
                j = pi_table[j]  # 다음 매칭을 위해 j 인덱스 조정
            else:
                j += 1  # 다음 문자로 넘어감
    
    return cnt  # 총 발견된 패턴의 횟수 반환