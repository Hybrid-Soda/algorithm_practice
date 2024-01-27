# 2839 설탕 배달
# 정확히 N을 맞추는 수 조합
# 최대한 적은 수 사용 / 수는 3과 5가 있음
# 3 <= N <= 5000 이므로 완전탐색 사용
# 1. 처음에 5를 모두 사용
# 2. 5로 나누어 떨어지지 않는다면 3을 빼고 5로 나눈다
# 3. 반복
# 4. 3을 뺐을 때 0보다 작아진다면 -1 출력

N = int(input())
count = 0

while True:
    # N이 0보다 클 때 계산 진행
    if N > 0:
        if N % 5 == 0:
            print(N//5 + count)
            break
        else:
            N -= 3
            count += 1
    # N이 0일 때 카운트한 숫자 출력
    elif N == 0:
        print(count)
        break
    # N이 0보다 작을 때 -1 출력
    else:
        print(-1)
        break