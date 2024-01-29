import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    hight = list(map(int, input().split()))
    secure = 0
    for i in range(2, N-2):
        max_value = max(hight[i - 2], hight[i - 1], hight[i + 1], hight[i + 2])
        if max_value <= hight[i]:
            secure += hight[i] - max_value
        else:
            pass
    
    print(f'#{tc} {secure}')
