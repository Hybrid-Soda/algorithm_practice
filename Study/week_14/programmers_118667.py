# 118667 두 큐 합 같게 만들기
from collections import deque

queue1 = [1, 2, 1, 2]
queue2 = [1, 10, 1, 2]

def solution(queue1, queue2):
    Q1 = deque(queue1)
    Q2 = deque(queue2)
    sumQ1 = sum(Q1)
    sumQ2 = sum(Q2)
    cnt = 0

    while True:

        # 하나의 배열이라도 비었다면 불가능
        if not (Q1 and Q2): return -1
        # 배열 속의 숫자 총 합이 홀수이면 불가능
        if (sumQ1 + sumQ2) & 1 : return -1

        # 두 큐의 합이 같으면 횟수 반환
        if sumQ1 == sumQ2: return cnt
        # 두 큐의 합이 다르면 큰 큐에서 작은 큐로 원소 이동
        elif sumQ1 > sumQ2:
            num = Q1.popleft()
            Q2.append(num)
            sumQ1
        elif sumQ1 < sumQ2:
            num = Q2.popleft()
            Q1.append(num)
        
        # 순환 구조라면 불가능
        if Q1 == deque(queue2): return -1

        cnt += 1

print(solution(queue1, queue2))