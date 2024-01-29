import sys
sys.stdin = open("input.txt")

for tc in range(1, int(input())+1):
    N = int(input())
    arr = list(map(int, input().split()))
    print(f'#{tc} {max(arr) - min(arr)}')