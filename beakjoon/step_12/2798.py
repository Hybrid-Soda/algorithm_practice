# 2798 블랙잭
# 각 카드 양의 정수 / N장의 카드 / M을 크게 외친다
# 제한된 시간 안에 N장의 카드 중 3장의 카드를 고름
# 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가까워야 한다
# 입력 : 첫째줄 - N과 M / 둘째줄 - 카드가 쓰여있는 수 <= 100,000
# 합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력
# 출력 : 첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
ans = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = numbers[i] + numbers[j] + numbers[k]
            if sum <= M and sum > ans:
                ans = sum

print(ans)