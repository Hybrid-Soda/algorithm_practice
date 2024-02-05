# 4874 Fourth

import sys
sys.stdin = open("input.txt")

for tc in range(int(input())):
    postfix = input().split()
    stack = []
    idx = 0

    for text in postfix:
        # text가 종료기호인 경우 남은 원소 개수에 따라 판단
        if text == '.':
            if len(stack) == 1:
                pass
            else:
                stack = ['error']
            break
        # text가 숫자인 경우 스택에 추가
        elif text.isdecimal() == True:
            stack.append(int(text))
        # text가 연산자인 경우
        else:
            try:
                # 뒤에서부터 원소를 뺀다
                back = stack.pop()
                front = stack.pop()
                # 사칙연산
                if text == '+':
                    stack.append(front + back)
                elif text == '-':
                    stack.append(front - back)
                elif text == '*':
                    stack.append(front * back)
                elif text == '/':
                    stack.append(front // back)
            except:
                stack = ['error']
        # 다음 text로 이동
        idx += 1
    
    print(f'#{tc+1} {stack[0]}')
