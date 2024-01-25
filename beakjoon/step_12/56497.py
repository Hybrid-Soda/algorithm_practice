# 56497 체스판 다시 칠하기
# M * N 크기의 체스판 -> 8 * 8 크기로 자름
# 다시 칠할 칸의 최소 개수

M, N = map(int, input().split())

board = [[input()] for _ in range()]

