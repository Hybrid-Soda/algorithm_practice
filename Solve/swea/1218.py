# 1218 괄호 짝짓기

import sys
sys.stdin = open('input.txt')

for tc in range(10):
    case_length = int(input())
    brackets = list(input())
    stack = []

    # 괄호 문자열 순회
    for bracket in brackets:
        # 스택이 비어있으면 현재 괄호 추가
        if not stack:
            stack.append(bracket)
        else:
            # 스택에 괄호가 있으면 현재 괄호와 비교하여 짝이 맞으면 제거
            if stack[-1] == '(' and bracket == ')':
                stack.pop()
            elif stack[-1] == '[' and bracket == ']':
                stack.pop()
            elif stack[-1] == '{' and bracket == '}':
                stack.pop()
            elif stack[-1] == '<' and bracket == '>':
                stack.pop()
            # 짝이 맞지 않으면 다른 괄호 추가
            else:
                stack.append(bracket)
    
    # 최종적으로 스택이 비어있으면 유효함 / 그렇지 않으면 유효하지 않음
    if len(stack) == 0:
        validation = 1
    else:
        validation = 0

    print(f'#{tc+1} {validation}')