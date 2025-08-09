import sys

sys.stdin = open('input.txt')


def find_start(x, y):
    while y == 0:
        dx = x - 1
        dy = y
        if ladder[dx][y - 1] == 1:
            dy -= 1

        if ladder[dx][y + 1] == 1:
            pass
    # # 범위 밖이거나, 벽이거나, 이미 방문한 경우
    # if x < 0 or x >= 100 or y < 0 or y >= 100:
    #     return False
    # if ladder[x][y] == 0 or visited[x][y]:
    #     return False
    # if ladder[x][y] == ladder[x][0]:
    #     return x
    #
    # visited[x][y] = True
    #
    # for dx, dy in [(0, 1), (0, -1), (-1, 0)]:
    #     if find_start(x + dx, y + dy):
    #         result_x = x + dx
    #         return result_x
    # return False


T = int(input())
for tc in range(1, T + 1):
    ladder = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False] * 100 for _ in range(100)]

    # 도착 지점 찾기
    goal_x = goal_y = 0
    for i in range(100):
        if ladder[99][i] == 2:
            goal_y = i
    result = find_start(99, goal_y)
    print(f'#{tc} {result}')
