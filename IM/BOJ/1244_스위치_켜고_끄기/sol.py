# 1244 스위치 켜고 끄기
# 목표: 입력되는 순서대로 자기의 성별과 받은 수에 따라 스위치의 상태를 바꾸었을 때,
# 스위치들의 마지막 상태를 출력

import sys
sys.stdin = open("input.txt")

N = int(input())  # N: 스위치 개수
switch = [0] + list(map(int, input().split()))  # 스위치 상태
S = int(input())  # S: 학생 수
student = [tuple(map(int, input().split())) for _ in range(S)]  # 성별, 받은 수

for gen, num in student:
    if gen == 1:  # 남자이면
        for i in range(num, N + 1, num):
            switch[i] = (switch[i] + 1) % 2
    else:  # 여자이면
        for i in range(N // 2):
            if i <= num < N - i + 1:
                part = switch[num - i : num + i + 1]
                if part != part[::-1]:
                    break
                else:
                    pass


print(*switch[1:])
