import sys
sys.stdin = open('input.txt')

# 6485 삼성시의 버스 노선
# N개의 버스 노선 / 5000개의 버스 정류장
# i번째 버스 노선은 번호가 A 이상, B 이하인 모든 정류장만을 다님
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 풀이

# 테스트 케이스
for tc in range(1, int(input())+1):
    # 버스 정류장 초기화
    bus_stop = {}
    for num in range(1, 5001):
        bus_stop[num] = 0

    # 루트 개수 입력 및 버스 정류장 카운트
    for route in range(int(input())):
        start, end = map(int, input().split())
        for num in range(start, end+1):
            bus_stop[num] += 1
    
    # 답 리스트에 추가
    answer = []
    for p in range(int(input())):
        answer.append(bus_stop[int(input())])


    print(f'#{tc}', *answer)
