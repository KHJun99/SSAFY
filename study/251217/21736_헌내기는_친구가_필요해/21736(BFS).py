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
from collections import deque


def bfs():
    global result

    delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = [[False] * M for _ in range(N)]

    q = deque()
    for r in range(N):
        for c in range(M):
            if zido[r][c] == 'I':
                q.append((r, c))
            if zido[r][c] == 'X':
                visited[r][c] = True

    while q:
        x, y = q.popleft()

        visited[x][y] = True
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny]:
                    if zido[nx][ny] == 'P':
                        visited[nx][ny] = True
                        q.append((nx, ny))
                        result += 1
                    if zido[nx][ny] == 'O':
                        visited[nx][ny] = True
                        q.append((nx, ny))


N, M = map(int, input().split())
zido = [input() for _ in range(N)]
result = 0

bfs()

print(result if result > 0 else 'TT')
