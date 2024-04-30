# 개인정보 수집 유효기간 (2023 KAKAO BLIND RECRUITMENT)

from datetime import datetime

def solution(today, terms, privacies):
    answer = []
    termsDict = {char.split()[0]: int(char.split()[1]) for char in terms}
    nowY, nowM, nowD = map(int, today.split('.'))

    for privacy in privacies:
        pre, var = privacy.split()
        preY, preM, preD = map(int, pre.split('.'))

        # if termsDict[var] > month:

    return answer


a = solution(
    "2022.05.19",
    ["A 6", "B 12", "C 3"],
    ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
)
print(a)