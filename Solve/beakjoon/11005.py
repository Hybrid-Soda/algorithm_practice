# 진법 변환 2
N, B = map(int, input().split())
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
arr = []

# N을 계속 B진법의 B로 나누어 나머지를 구하면 된다
if N < B:
    print(number[N])
else:
    while N > 0:
        remain = N % B
        N = int((N - remain) / B)
        arr.append(number[remain])
arr.reverse()

print(''.join(arr))