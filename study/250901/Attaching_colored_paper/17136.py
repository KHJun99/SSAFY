# 백준_17136_색종이 붙이기 (G2)
"""
1. 문제 상황

- 크기가 10 × 10인 격자판이 주어진다.
- 각 칸은 0(빈칸) 또는 1(채워야 하는 칸)으로 구성된다.
- 우리는 1×1, 2×2, 3×3, 4×4, 5×5 크기의 색종이를 사용할 수 있다.
- 단, 각 색종이는 최대 5장까지만 사용 가능하다.
- 목표는 모든 1이 적힌 칸을 색종이로 덮는 것.
- 색종이를 격자판에 붙일 때는 칸에 맞게 정확히 붙어야 하며, 격자 밖으로 나가면 안 되고, 0인 칸 위를 덮을 수도 없다.

2. 출력

- 모든 1 칸을 색종이로 덮을 수 있다면, 사용한 색종이의 최소 개수를 출력한다.
- 덮을 수 없다면 -1을 출력한다.

3. 조건

- 색종이는 정사각형 형태여야 한다.
- 색종이는 겹칠 수 없다.
- 색종이를 붙이는 과정에서 부분적으로 0을 덮으면 안 된다.
- 사용할 수 있는 색종이 개수는 크기별 최대 5장.
"""
import sys
input = sys.stdin.readline

# 10x10 보드 입력
board = [list(map(int, input().split())) for _ in range(10)]

# 각 크기(1~5) 별 남은 색종이 개수 (문제: 각 5장)
left = [0, 5, 5, 5, 5, 5]

INF = 10**9
answer = INF

def find_next_one(bd):
    """다음으로 덮어야 할 '1'의 첫 위치를 찾는다. 없으면 (-1, -1)"""
    for i in range(10):
        for j in range(10):
            if bd[i][j] == 1:
                return i, j
    return -1, -1

def can_place(bd, x, y, size):
    """(x,y)에서 size x size 정사각형을 붙일 수 있는지 검사"""
    if x + size > 10 or y + size > 10:
        return False
    for i in range(x, x + size):
        for j in range(y, y + size):
            if bd[i][j] != 1:      # 하나라도 1이 아니면 불가
                return False
    return True

def place(bd, x, y, size, val):
    """(x,y)에서 size x size 영역을 val(0 또는 1)로 채움"""
    for i in range(x, x + size):
        for j in range(y, y + size):
            bd[i][j] = val

def dfs(used):
    """
    used: 지금까지 사용한 색종이 수
    전략:
      1) 다음 1 위치를 찾는다.
      2) 없으면 모든 1을 덮은 것이므로 answer 갱신.
      3) 있으면 큰 size(5)부터 가능한 것만 붙여보고 백트래킹.
    """
    global answer

    # 가지치기: 이미 최소 해보다 많이 사용 중이면 중단
    if used >= answer:
        return

    x, y = find_next_one(board)
    if x == -1:
        # 모든 1을 덮었다
        answer = min(answer, used)
        return

    # 큰 색종이부터 시도 (탐색 수 감소)
    for size in range(5, 1 - 1, -1):
        if left[size] == 0:
            continue
        if not can_place(board, x, y, size):
            continue

        # 붙이기
        place(board, x, y, size, 0)
        left[size] -= 1

        dfs(used + 1)

        # 복구
        left[size] += 1
        place(board, x, y, size, 1)

# 실행
dfs(0)
print(-1 if answer == INF else answer)

# def find_paper(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst[i])):
#             if lst[i][j] == 1:
#                 return(i, j)
#
# def size_of_paper(lst, x, y):
#     global num_of_paper
#
#     for size in range(5, 0, -1):
#         temp = lst[:]
#         for r in range(x, x + size):
#             for c in range(y, y + size):
#                 if lst[r][c] == 1:
#                     temp[r][c] = 0
#
#
# paper = [list(map(int, input().split())) for _ in range(10)]
# # 필요한 종이 개수
# num_of_paper = 0
#
# # 사이즈별 종이 개수
# size_paper = [5] * 6
#
# position = find_paper(paper)
# size_of_paper(paper, position[0], position[1])
# print(num_of_paper)
