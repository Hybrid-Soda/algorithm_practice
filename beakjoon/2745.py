# 진법 변환

N, B = input().split()
N, B = ''.join(reversed(N)), int(B)

number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ans = 0

for i in range(len(N)):
    ans += (number.index(N[i]) * B ** i)

print(ans)