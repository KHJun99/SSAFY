# [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리
def find_goal(x, y):
    count = 0
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    if x < 0 or x >= N or y < 0 or y >= N:
        return 0
    if maze[x][y] == 1 or visited[x][y]:
        return 0
    if maze[x][y] == 3:
        return count

    visited[x][y] = True
    count += 1

    for dx, dy in delta:
        if find_goal(x + dx, y + dy):
            return count
    return 0

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # 출발 좌표 구하기
    start_x = N-1
    for row in range(N):
        for col in range(N):
            if maze[row][col] == 2:
                start_y = col
    

    result = find_goal(start_x, start_y)

    print(f'#{tc} {result}')
    