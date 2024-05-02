# 크레인 인형뽑기 게임 (2019 카카오 개발자 겨울 인턴십)

def solution(board, moves):
    ans = 0
    stack = []
    for j in moves:
        i = 0
        j -= 1
        while i < len(board):
            if board[i][j]:
                stack.append(board[i][j])
                board[i][j] = 0
                break
            i += 1

        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack.pop()
            stack.pop()
            ans += 2

    return ans


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))