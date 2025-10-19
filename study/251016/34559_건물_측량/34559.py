# 백준_34559_건물_측량 (G3)
"""
## [문제 정리]
- 관우는 땅과 건물이 그려져 있는 N x M 크기의 지도를 가지고 있다.
    - 지도의 가장 왼쪽 위 : (1, 1)
    - 지도의 가장 오른쪽 아래 : (N, M)
- 지도에서 건물을 표시하는 방법
    - 1로 표현된 칸
    - 0으로 표현된 칸 중에서 상하좌우 인접한 0으로 이동해 지도의 테두리에 도달할 수 없는 칸
- 지도의 테두리란?
    - 1번째 행, N번째 행, 1번째 열, M번째 열
    - 위 4가지 중 하나 이상에 포함되는 칸을 의미
- 지도의 테두리와 위 기준에 포함되지 않는 모든 칸은 땅을 의미
- 임의의 두 좌표로 만들어지는 직사각형 모양의 범위에 새건물을 지을려고 한다.
    - 직사각형에 포함되는 모든 칸에 건물이 포함되지 않아야 한다.
"""
# 사간초과
# import sys
# input = sys.stdin.readline
#
#
# def find_house():
#     global zido
#     delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     for i in range(N + 1):
#         for j in range(M + 1):
#             if zido[i][j] == 0:
#                 count = 0
#                 for dx, dy in delta:
#                     nx, ny = i + dx, j + dy
#                     if 0 <= nx <= N and 0 <= ny <= M and zido[nx][ny] == 1:
#                         count += 1
#                 if count == 4:
#                     zido[i][j] = 1
#
#
# def check(r1, c1, r2, c2):
#     count = 0
#     is_build = 'Yes'
#     for i in range(r1, r2 + 1):
#         for j in range(c1, c2 + 1):
#             if zido[i][j] == 1:
#                 count += 1
#
#     if count != 0:
#         is_build = 'No'
#         return is_build, count
#
#     return is_build
#
#
# N, M = map(int, input().split())
# zido = [[0] * (M + 1) for _ in range(N + 1)]
# for i in range(1, N + 1):
#     row = list(input())
#     for j in range(1, M + 1):
#         zido[i][j] = int(row[j - 1])
#
# Q = int(input())
# coordinate = []
# for _ in range(Q):
#     r1, c1, r2, c2 = map(int, input().split())
#     coordinate.append((r1, c1, r2, c2))
#
# find_house()
# for idx in coordinate:
#     result = check(idx[0], idx[1], idx[2], idx[3])
#     if result != 'Yes':
#         print(*result)
#     else:
#         print(result)
#----------------------------------------------------
from collections import deque
import sys
input = sys.stdin.readline

def fill_house():
    global visited, zido
    q = deque([(0, 0)])
    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    while q:
        x, y = q.popleft()

        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= N and 0 <= ny <= M and not visited[nx][ny] and zido[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx, ny))

    for i in range(N + 1):
        for j in range(M + 1):
            if visited[i][j] == False and zido[i][j] != 1:
                zido[i][j] = 1


def prefix_sum():
    ps = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        hap = 0
        for j in range(1, M + 1):
            hap += zido[i][j]
            ps[i][j] = ps[i-1][j] + hap
    return ps

def ps_sum(ps, a, b, c, d):
    return ps[c][d] - ps[a-1][d] - ps[c][b-1] + ps[a-1][b-1]

N, M = map(int, input().split())
zido = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    row = list(input())
    for j in range(1, M + 1):
        zido[i][j] = int(row[j - 1])

Q = int(input())
visited = [[False] * (M + 1) for _ in range(N + 1)]

fill_house()

ps = prefix_sum()

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    result = ps_sum(ps, r1, c1, r2, c2)

    if result == 0:
        print('Yes')
    else:
        print(f'No {result}')
