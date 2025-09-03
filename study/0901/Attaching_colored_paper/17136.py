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
from collections import deque
def square(lst,x , y):
    n = 10
    for size in range(5, 0, -1):
        for r in range(n - size + 1):
            for c in range(n - size + 1):
                sub_paper = [row[c:c+size] for row in lst[r:r+size]]




# def bfs(lst):
#     for r in range(10):
#         for c in range(10):
#             if lst[r][c] == 1:


paper = [list(map(int, input().split())) for _ in range(10)]

print(all(paper))