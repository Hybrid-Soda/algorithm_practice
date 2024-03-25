# [HSAT 5회 정기 코딩 인증평가 기출] 성적 평가

# 주어진 배열의 점수들의 순위를 계산하고 출력하는 함수
def compute_ranking(arr):
    ranking = [0] * n  # 순위 리스트
    ans = [0] * n  # 최종 순위 리스트
    
    # 각 점수에 해당하는 인덱스를 할당
    for i in range(n):
        arr[i] = [arr[i], i]
    
    arr.sort(reverse=True)  # 내림차순 정렬
    cnt = 1  # 순위 카운터 초기화
    ranking[0] = 1

    for i in range(1, n):
        # 현재 점수가 이전 점수와 다른 경우, 순위 카운터 업데이트
        if arr[i][0] != arr[i-1][0]:
            cnt = i + 1
        # 현재 순위를 해당하는 인덱스에 할당
        ranking[i] = cnt
    
    # 원래 순서에 따라 최종 순위를 'ans'에 할당
    for i in range(n):
        ans[arr[i][1]] = ranking[i]
    
    # 최종 순위 출력
    for i in range(n):
        print(ans[i], end=' ')
    print()

n = int(input())
total = [0] * n

for _ in range(3):
    scores = list(map(int, input().split()))
    for i in range(n):
        total[i] += scores[i]
    compute_ranking(scores)  # 현재 경기 순위를 계산하고 출력

compute_ranking(total)  # 전체 순위를 계산하고 출력



# 시간초과 코드 - index() 메서드로 인한 시간초과
'''
def compute_ranking(arr):
    new_arr = sorted(arr, reverse=True)
    print(*[new_arr.index(arr[i]) + 1 for i in range(n)])

n = int(input())
total = [0] * n

for _ in range(3):
    scores = list(map(int, input().split()))
    for i in range(n): total[i] += scores[i]
    compute_ranking(scores)

compute_ranking(total)
'''