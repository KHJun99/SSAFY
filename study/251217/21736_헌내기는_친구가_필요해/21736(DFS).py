# 백준_21736_헌내기는_친구가_필요해 (S2)
"""
## [문제 정리]
- 도연이가 다니는 대학의 캠퍼스틑 N x M 크기
- 캠퍼스에서 이동하는 방법
    - 벽이 아닌 상하좌우로 이동
    - 예시
        - 도연이가 (x, y)에 있다면,
        - 이동 가능 범위 : (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)
    - 단, 캠퍼스 밖으로는 이동 불가능
- 도연이가 만날 수 있는 사람의 수를 구하시오.
"""
import sys
sys.setrecursionlimit(10**6)

def dfs(row, col):
    global result

    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    if zido[row][col] == 'P':
        result += 1

    for dx, dy in delta:
        nx, ny = row + dx, col + dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and zido[nx][ny] != 'X':
            visited[nx][ny] = True
            dfs(nx, ny)


N, M = map(int, input().split())
zido = [input() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
result = 0

Dx, Dy = 0, 0
for r in range(N):
    for c in range(M):
        if zido[r][c] == 'I':
            Dx, Dy = r, c
            visited[r][c] = True
            break

dfs(Dx, Dy)

print(result if result > 0 else 'TT')