# 백준_2667_단지번호붙이기 (s1)
"""
문제 정의

정사각형 형태의 지도가 주어진다.
지도에서 1은 집이 있는 곳, 0은 집이 없는 곳을 의미한다.
집들이 상하좌우로 인접하면 하나의 단지로 묶인다.
대각선은 연결로 취급하지 않는다.

목표

1. 지도의 집들을 기준으로 몇 개의 단지가 있는지 구한다.
2. 각 단지에 속하는 집의 수를 계산한다.
3. 그 수를 오름차순으로 정렬하여 출력한다.
"""
from collections import deque

N = int(input())
grid = [list(input().strip()) for _ in range(N)]

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * N for _ in range(N)]

house = []

# BFS
for r in range(N):
    for c in range(N):
        if grid[r][c] == '1' and not visited[r][c]:
            # 단지 시작
            q = deque([(r, c)])
            visited[r][c] = True
            cnt = 1

            while q:
                x, y = q.popleft()
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        if not visited[nx][ny] and grid[nx][ny] == '1':
                            visited[nx][ny] = True
                            q.append((nx, ny))
                            cnt += 1

            house.append(cnt)

house.sort()
print(len(house))
for idx in house:
    print(idx)