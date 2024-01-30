import sys
sys.stdin = open("input.txt")

for tc in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))
    secure = 0
    for i in range(2, N-2):
        max_value = max(height[i - 2], height[i - 1], height[i + 1], height[i + 2])
        if max_value < height[i]:
            secure += height[i] - max_value
        else:
            pass
    
    print(f'#{tc} {secure}')
