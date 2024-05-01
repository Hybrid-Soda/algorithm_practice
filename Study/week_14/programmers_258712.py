# 가장 많이 받은 선물 (2024 KAKAO WINTER INTERNSHIP)

def solution(friends, gifts):
    N = len(friends)
    manIdx = {f: i for i, f in enumerate(friends)}
    giftIst = [[0] * N for _ in range(N)]
    giftIdx = [0] * N

    for gift in gifts:
        give, take = gift.split()
        i, j = manIdx[give], manIdx[take]
        giftIst[i][j] += 1
        giftIdx[i] += 1
        giftIdx[j] -= 1

    answer = 0
    return answer

a = solution(["muzi", "ryan", "frodo", "neo"],
             ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", 
              "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])
print(a)  # 2