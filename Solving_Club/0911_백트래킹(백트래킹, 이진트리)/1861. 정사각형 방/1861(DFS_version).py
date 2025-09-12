# 정사각형 방 - DFS
# -> 원래는 시간 초과가 나야 하는데 학습용으로 공유 드립니다!!!

# [선물] BFS 방식은 직접 구현 해보세요! 😊

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def dfs(sy, sx):
    global matrix, cnt
    for i in range(4):
        ny, nx = sy + dy[i], sx + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if matrix[ny][nx] == matrix[sy][sx] + 1:
                cnt += 1
                dfs(ny, nx)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_cnt, resulty, resultx = 0, 0, 0
    for y in range(N):
        for x in range(N):
            cnt = 1
            dfs(y, x)
            if max_cnt < cnt:
                max_cnt = cnt
                resulty = y
                resultx = x
            elif max_cnt == cnt and matrix[y][x] < matrix[resulty][resultx]:
                resulty = y
                resultx = x

    print(f'#{tc} {matrix[resulty][resultx]} {max_cnt}')