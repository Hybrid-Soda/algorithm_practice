# 1158 요세푸스 문제
# (N,K) 요세푸스 순열을 구하시오

# N : 사람 수 / K : 제거되는 사람 번호
N, K = map(int, input().split())
people = [i+1 for i in range(N)]
josephus = []
num = 0

while people:
    num = (num + K - 1) % len(people)
    josephus.append(people.pop(num))

print(f"<{', '.join(map(str, josephus))}>")