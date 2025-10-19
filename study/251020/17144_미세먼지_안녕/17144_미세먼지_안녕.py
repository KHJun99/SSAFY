# 백준_미세먼지_안녕 (G4)
"""
## [문제 정리]
- 집의 크기 : R x C 인 격자판 ( 1 x 1 크기의 칸으로 나눔 )
    - (r, c)는 r행 c열을 의미
- 공기청정기는 항상 1번 열에 설치되어 있고, 두 행을 차지
- 공기청정기가 설치되어 있지 않은 칸에는 미세먼지 존재
    (r, c)에 있는 미세먼지 양은 A_(r,c)

- 1초 동안 아래 적힌 일이 순서대로 진행
    1. 미세먼지 확산 ( 확산은 미세먼지가 있는 모든 칸에서 동시에 일어남 )
        - (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산
        - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 확산 X
        - 확산되는 양 = A_(r,c)/5 ( 소수점은 버린다 )
        - (r, c)에 남은 미세먼지 양 = A_(r,c) - A_(r,c)/5 * (확산된 방향의 개수)
    2. 공기청정기가 작동
        - 바람이 나온다.
        - 위쪽 공기청정기에서는 바람이 반시계방향으로 순환
        - 아래쪽 공기청정기의 바람은 시계방향으로 순환
        - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
        - 공기청정기에서 부는 바람은 미세먼지가 없는 바람
        - 공기청정기로 들어간 미세먼지는 모두 정화

- 방의 정보가 주어졌을 때, T초가 지난 후 방에 남아있는 미세먼지양을 구하시오.
"""
def diffuse(board):
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    new = [[0] * C for _ in range(R)]
    # 공기청정기 고정
    new[upper][0] = -1
    new[lower][0] = -1

    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                plus = board[r][c] // 5
                moved = 0
                for dr, dc in delta:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != -1:
                        new[nr][nc] += plus
                        moved += 1
                new[r][c] += board[r][c] - (plus * moved)
    return new

def move_air(board):
    """공기청정기 바람 순환 (upper=반시계, lower=시계)"""

    # 위쪽 순환: 오른 → 위 → 왼 → 아래
    # 아래 → 위 (왼쪽 세로줄)
    for r in range(upper - 1, 0, -1):
        board[r][0] = board[r - 1][0]
    # 왼 → 오른쪽 (맨 윗줄)
    for c in range(0, C - 1):
        board[0][c] = board[0][c + 1]
    # 위 → 아래 (오른쪽 세로줄)
    for r in range(0, upper):
        board[r][C - 1] = board[r + 1][C - 1]
    # 오른 → 왼쪽 (upper 행)
    for c in range(C - 1, 1, -1):
        board[upper][c] = board[upper][c - 1]
    board[upper][1] = 0  # 흡입구 옆 칸 정화 공기 주입

    # 아래쪽 순환: 오른 → 아래 → 왼 → 위
    # 위 → 아래 (왼쪽 세로줄)
    for r in range(lower + 1, R - 1):
        board[r][0] = board[r + 1][0]
    # 왼 → 오른쪽 (맨 아랫줄)
    for c in range(0, C - 1):
        board[R - 1][c] = board[R - 1][c + 1]
    # 아래 → 위 (오른쪽 세로줄)
    for r in range(R - 1, lower, -1):
        board[r][C - 1] = board[r - 1][C - 1]
    # 오른 → 왼쪽 (lower 행)
    for c in range(C - 1, 1, -1):
        board[lower][c] = board[lower][c - 1]
    board[lower][1] = 0  # 흡입구 옆 칸 정화 공기 주입

    # 공기청정기 위치 복원
    board[upper][0] = -1
    board[lower][0] = -1

R, C, T = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(R)]

# 공기청정기 위치
air = []
for r in range(R):
    if house[r][0] == -1:
        air.append(r)
upper, lower = air[0], air[1]

for _ in range(T):
    house = diffuse(house)
    move_air(house)

# 합계(공기청정기 -1 제외)
ans = 0
for i in range(R):
    for j in range(C):
        if house[i][j] > 0:
            ans += house[i][j]
print(ans)