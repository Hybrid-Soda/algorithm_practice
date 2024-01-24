# 2292 벌집
# 1(layer1) - 6(layer2) - 12(layer3) - 18(layer4) - 24(layer5) - ...
# 6n의 합 sum(n) = n(n-1)/2 이므로 s
# 최종번호에서 6의 배수씩 뺄셈하면 된다

N = int(input())
layer = 1

while N > 1:
    N -= 6 * layer
    layer += 1
    
print(layer)