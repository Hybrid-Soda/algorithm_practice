# 1945 간단한 소인수분해
# 2,3,5,7,11 의 몇승인지 확인
# a,b,c,d,e 출력
import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N = int(input())
    count = [0] * 5

    while N != 0:
        if N % 2 == 0:
            N //= 2
            count[0] += 1
        elif N % 3 == 0:
            N //= 3
            count[1] += 1
        elif N % 5 == 0:
            N //= 5
            count[2] += 1
        elif N % 7 == 0:
            N //= 7
            count[3] += 1
        elif N % 11 == 0:
            N //= 11
            count[4] += 1
        else:
            break

    print(f'#{tc+1}', *count)