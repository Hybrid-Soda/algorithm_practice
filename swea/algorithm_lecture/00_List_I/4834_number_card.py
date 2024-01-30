# 4834 숫자카드
# N장의 카드 (0~9)
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력 / 개수 같을 때는 적힌 숫자가 큰 쪽을 출력

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    N = int(input())
    numbers = list(input())
    # 개수 같을 때는 적힌 숫자가 큰 것을 고르기 위해 내림차순 정렬
    numbers.sort(reverse=True)
    # ans[0] : 가장 많은 카드의 숫자 / ans[1] : 장 수
    ans = [0, 0]
    count = 1

    # 숫자 카드의 개수-1 만큼 진행 (바로 다음카드와 비교하므로)
    for i in range(len(numbers)-1):
        # 현재카드와 다음카드의 숫자가 같다면
        if numbers[i] == numbers[i+1]:
            # 현재 숫자의 동일 카드 개수 +1
            count += 1
        # 현재카드와 다음카드의 숫자가 다르다면
        else:
            # 카드 개수 초기화
            count = 1
        # 만약 현재카드 숫자의 동일 카드 개수가 이전보다 많다면 업데이트
        if count > ans[1]:
            ans[0] = numbers[i]
            ans[1] = count

    print(f'#{tc+1}', *ans)