# 백준_14503_로봇_청소기 (G5)
"""
## [문제 정리]

- 방 사이즈 : N x M (1 x 1 크기의 정사각형 칸으로 나누어져 있다.)
- 각각의 칸은 벽 또는 빈 칸
- 청소기
    - 바라보는 방향 존재 (동, 서, 남, 북 중 하나)
- 로봇 청소기 작동 순서
    1. 현재 칸이 청소되지 않은 경우, 현재 칸 청소
    2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우
        - 바라보는 방향 유지 -> 후진 가능 -> 한 칸 후진 후 1번으로 돌아감
        - 바라보는 방향의 뒤쪽 칸이 벽이라 후진 불가능 -> 작동을 멈춘다.
    3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸 존재
        - 반시계 방향으로 90도 회전
        - 바라보는 방향 기준 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진
        - 1번으로 돌아간다.

- 로봇 청소기와 방의 상태가 주어졌을 때, 청소하는 영역의 개수를 구하는 프로그램 작성
"""
# 방의 크기
N, M = map(int, input().split())

# 로봇 청소기 좌표와 방향
r, c, d = map(int, input().split())

# 방 상태 (0: 청소 안 됨, 1: 벽, 2: 청소 완료)
room = [list(map(int, input().split())) for _ in range(N)]

# 북(0), 동(1), 남(2), 서(3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = 0

while True:
    # 1. 현재 칸이 청소되지 않은 경우, 청소
    if room[r][c] == 0:
        room[r][c] = 2
        ans += 1

    # 2. 주변 4칸 확인
    cleaned_all = True
    for _ in range(4):
        # 반시계 방향으로 90도 회전
        d = (d + 3) % 4
        nr, nc = r + dx[d], c + dy[d]

        # 앞쪽 칸이 청소되지 않은 빈 칸인 경우
        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0:
            r, c = nr, nc
            cleaned_all = False
            break

    # 3. 네 방향 모두 청소되어 있거나 벽인 경우
    if cleaned_all:
        # 후진
        back_d = (d + 2) % 4
        br, bc = r + dx[back_d], c + dy[back_d]

        # 후진할 수 있으면 후진
        if 0 <= br < N and 0 <= bc < M and room[br][bc] != 1:
            r, c = br, bc
        else:
            # 후진할 수 없으면 작동 중지
            break

print(ans)
