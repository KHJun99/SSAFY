# 백준_1520_내리막_길 (G3)
"""
## [문제 정리]
- 지도는 직사각형 모양
- 한 칸은 한 지점을 나타내고 각 칸에는 그 지점의 높이
- 각 지점 사이의 이동은 지도에서 상하좌우 이웃한 곳끼리만 가능
- 세준이는 제일 왼쪽 위 칸에서 제일 오른쪽 아래로 이동하려고 한다.
    - 항상 높이가 더 낮은 지점으로만 이동 가능

- 제일 왼쪽 위 지점에서 출발하여 제일 오른족 아래 지점까지 항상 내리막길로만
- 이동하는 경로의 개수를 구하는 프로그램 작성
"""
import sys
sys.setrecursionlimit(10**6)


def dfs(r, c):
    if r == N - 1 and c == M - 1:
        return 1

    if dp[r][c] != -1:
        return dp[r][c]

    dp[r][c] = 0

    for idx in range(4):
        nr, nc = r + dr[idx], c + dc[idx]

        if 0 <= nr < N and 0 <= nc < M and zido[r][c] > zido[nr][nc]:
            dp[r][c] += dfs(nr, nc)

    return dp[r][c]


N, M = map(int, input().split())
zido = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

result = dfs(0, 0)

print(result)