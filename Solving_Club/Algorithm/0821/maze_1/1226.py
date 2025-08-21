# [S/W 문제해결 기본] 7일차 - 미로 1 (D4)
"""
문제
아래 그림과 같은 미로가 있다. 16*16 행렬의 형태로 만들어진 미로에서 흰색 바탕은 길, 노란색 바탕은 벽을 나타낸다.
가장 좌상단에 있는 칸을 (0, 0)의 기준으로 하여, 가로방향을 x 방향, 세로방향을 y 방향이라고 할 때, 미로의 시작점은 (1, 1)이고 도착점은 (13, 13)이다.
주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램을 작성하라.
"""
import sys
from collections import deque
sys.stdin = open('input.txt')


def find_maze(sx, sy, maze):
    N = len(maze)
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * N for _ in range(N)]

    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for dx, dy in delta:
            nx, ny = x + dx, y + dy

            # 1) 경계 체크
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            # 2) 벽(1)은 통과 불가
            if maze[nx][ny] == 1:
                continue
            # 3) 이미 방문했으면 패스
            if visited[nx][ny]:
                continue

            # 4) 목표(3) 도달
            if maze[nx][ny] == 3:
                return 1

            # 5) 길(0) 혹은 시작(2)라면 큐에 추가
            visited[nx][ny] = True
            q.append((nx, ny))

    return 0


T = 10
for _ in range(T):
    tc = int(input())

    # 16줄을 읽되, 공백 유무에 상관없이 파싱되게 처리
    maze = []
    for _ in range(16):
        line = input().strip()
        if ' ' in line:
            row = list(map(int, line.split()))
        else:
            row = list(map(int, line))  # '010201...' 형태
        maze.append(row)

    # 시작점(2) 찾기
    sx = sy = 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sx, sy = i, j
                break

    result = find_maze(sx, sy, maze)
    print(f'#{tc} {result}')
