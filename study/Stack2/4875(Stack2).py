# [파이썬 S/W 문제해결 기본] 5일차 - 미로
def backtrack(n):
    visited = [[[False] for _ in range(n)] for _ in range(n)]
    pass

# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())
#     maze = [(list(map(int, input().split()))) for _ in range(N)]
#     delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     for i in range(N):
#         for j in range(N):
#             if maze[i][j] == 2:     # 출발점 찾기
#                 stack = [(i, j)]
#                 break

stack = (1,0)
delta = (1,0)
print(list(zip(stack,delta)))