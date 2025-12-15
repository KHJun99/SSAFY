# 백준_2573_빙산 (G4)
"""
## [문제 정리]

- 빙산의 각 부분별 높이 정보는 배열의 각 칸에 양의 정수로 저장
- 빙산 이외의 바다에 해당되는 칸에는 0이 저장

- 빙산의 높이는 바닷물에 많이 접해있는 부분에서 더 빨리 감소
    - 빙산의 각 부분에 해당되는 칸에 있는 높이는 일년마다
    - 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
    - 단, 각 칸에 저장된 높이는 0보다 더 줄어들지 않는다.
    - 바닷물은 호수처럼 빙산에 둘러싸여 있을 수도 있다.
- 한 덩어리의 빙산이 주어질 때, 이 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하시오.
- 만약, 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 프로그램은 0을 출력
"""
# 백준_2573_빙산 (G4)
from collections import deque


def melting():
    global iceberg

    # 녹는 양을 먼저 계산 (동시에 녹아야 하므로)
    melt_amount = [[0] * M for _ in range(N)]

    for r in range(N):
        for c in range(M):
            if iceberg[r][c] > 0:
                cnt = 0
                for dx, dy in delta:
                    nr, nc = r + dx, c + dy
                    if 0 <= nr < N and 0 <= nc < M and iceberg[nr][nc] == 0:
                        cnt += 1
                melt_amount[r][c] = cnt

    # 계산된 양만큼 녹이기
    for r in range(N):
        for c in range(M):
            iceberg[r][c] = max(0, iceberg[r][c] - melt_amount[r][c])


def count_islands():
    visited = [[False] * M for _ in range(N)]
    island_cnt = 0

    for r in range(N):
        for c in range(M):
            if iceberg[r][c] > 0 and not visited[r][c]:
                # 새로운 섬 발견
                island_cnt += 1

                # BFS로 연결된 모든 빙산 탐색
                queue = deque([(r, c)])
                visited[r][c] = True

                while queue:
                    x, y = queue.popleft()

                    for dx, dy in delta:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < M:
                            if iceberg[nx][ny] > 0 and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))

    return island_cnt


N, M = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(N)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

year = 0
while True:
    # 빙산의 개수 확인
    island_count = count_islands()

    # 빙산이 두 개 이상으로 분리
    if island_count >= 2:
        print(year)
        break

    # 빙산이 모두 녹았으면
    if island_count == 0:
        print(0)
        break

    # 1년 경과
    melting()
    year += 1



