# 백준_2146_다리_만들기 (G3)
"""
## [문제 정리]
- 바다에 여러 섬이 존재한다.
- 대통령 공략 : 섬과 섬을 이을 다리를 짓겠다.
- 비용이 아까워 단 1개의 다리만 지을 예정
- 가장 짧은 다리 하나를 놓아 두 대륙을 연결하는 방법을 찾으시오.
"""
from collections import deque

def labeling_island():
    global zido

    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    n = 2
    for r in range(N):
        for c in range(N):
            if zido[r][c] == 1:
                q = deque([(r, c)])
                zido[r][c] = n

                while q:
                    cx, cy = q.popleft()
                    for dx, dy in delta:
                        nx, ny = dx + cx, dy + cy
                        if 0 <= nx < N and 0 <= ny < N and zido[nx][ny] == 1:
                            zido[nx][ny] = n
                            q.append((nx, ny))
                n += 1

def bfs():
    global min_bridge

    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * N for _ in range(N)]

    q = deque()

    for r in range(N):
        for c in range(N):
            island_num = 2
            if zido[r][c] == island_num:
                visited[r][c] = True
                q.append((r, c))
                tmp = []
                cnt = 0

                while q:
                    cx, cy = q.popleft()
                    for dx, dy in delta:
                        nx, ny = dx + cx, dy + cy
                        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and zido[nx][ny] == 0:
                            visited[nx][ny] = True
                            tmp.append((nx, ny))
                            q.append((nx, ny))
                            cnt += 1

                        if zido[nx][ny] != 0 and zido[nx][ny] != island_num:
                            min_bridge = min(min_bridge, cnt)


N = int(input())

zido = [list(map(int, input().split())) for _ in range(N)]

min_bridge = float('inf')

labeling_island()

bfs()

print(min_bridge)

