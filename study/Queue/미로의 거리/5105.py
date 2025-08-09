# [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
# deque를 사용해서 queue 활용
from collections import deque
import sys

sys.stdin = open('sample_input.txt')


def find_goal(x, y):
    queue = deque([(x, y, 0)])  # (x, y, 이동 횟수)
    visited = [[False] * N for _ in range(N)]
    visited[x][y] = True
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위

    while queue:
        cx, cy, steps = queue.popleft()
        if maze[cx][cy] == 3:
            return steps - 1  # 시작점, 도착점을 제외한 이동 횟수 반환

        for dx, dy in delta:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maze[nx][ny] != 1:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))

    return 0  # 경로가 없을 경우


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    # 시작점 찾기
    start_x = start_y = 0
    for row in range(N):
        for col in range(N):
            if maze[row][col] == 2:
                start_x, start_y = row, col

    result = find_goal(start_x, start_y)
    print(f'#{tc} {result}')