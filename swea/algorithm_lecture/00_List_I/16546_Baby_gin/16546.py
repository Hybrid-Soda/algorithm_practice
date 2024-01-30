import sys
sys.stdin = open("input.txt")

T = int(input())


def babygin(numbers):
    counter = [0]*10
    count_babygin = 0

    for number in numbers:
        counter[number] += 1

    idx = 0
    while idx < len(counter):
        if counter[idx] >= 3:
            counter[idx] -= 3
            count_babygin += 1
            idx = 0
            continue
        if idx < 8 and (counter[idx] and counter[idx+1] and counter[idx+2]):
            counter[idx] -= 1
            counter[idx+1] -= 1
            counter[idx+2] -= 1
            count_babygin += 1
            idx = 0
            continue
        if count_babygin == 2:
            return "true"
        idx += 1
    if count_babygin != 2:
        return "false"


for tc in range(1, T+1):
    number_list = list(map(int, input()))
    ans = babygin(number_list)
    print(f"#{tc} {ans}")
