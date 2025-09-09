# [파이선 S/W 문제해결 기본] 6일차 - 미로의 거리
"""
문제
NxN 크기의 미로에서 출발지 목적지가 주어진다.
이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
"""
import sys
sys.stdin = open('5105_input.txt')
from collections import deque


def find_pos(grid, n):
    sr = sc = gr = gc = -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '2':
                sr, sc = i, j
            elif grid[i][j] == '3':
                gr, gc = i, j
    return (sr, sc), (gr, gc)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(input().strip()) for _ in range(N)]

    (sr, sc), (gr, gc) = find_pos(maze, N)

    # BFS 준비
    q = deque([(sr, sc)])
    visited = [[False] * N for _ in range(N)]
    dist = [[-1] * N for _ in range(N)]

    visited[sr][sc] = True
    dist[sr][sc] = 0

    # 상하좌우
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    ans = 0  # 도달 못 하면 0
    while q:
        r, c = q.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                # 벽('1')만 막고, 나머지('0','3')는 진행
                if not visited[nr][nc] and maze[nr][nc] != '1':
                    visited[nr][nc] = True
                    dist[nr][nc] = dist[r][c] + 1

                    if maze[nr][nc] == '3':
                        # 시작/도착을 제외한 칸 수
                        ans = dist[nr][nc] - 1
                        q.clear()  # 즉시 종료
                        break
                    q.append((nr, nc))

    print(f"#{tc} {ans}")

