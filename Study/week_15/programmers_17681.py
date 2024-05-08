# [1차] 비밀지도 (2018 KAKAO BLIND RECRUITMENT)

def solution(n, arr1, arr2):
    # print([bin(arr1[i] | arr2[i]).replace('1', '#').split('0')[2:] for i in range(n)])
    return [' '.join(bin(arr1[i] | arr2[i]).replace('1', '#').split('0'))[2:] for i in range(n)]

print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))