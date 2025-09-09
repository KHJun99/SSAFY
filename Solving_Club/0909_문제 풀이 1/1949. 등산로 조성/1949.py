# [모의 SW 역량 테스트] 등산로 조성
"""
문제
- N * N 크기의 부지에 최대한 긴 등산로를 만들 계획
- 등산로 규칙
    - 등산로는 가장 높은 봉우리에서 시작
    - 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결
      (즉, 높이가 같은 곳 혹은 낮은 지형, 대각선 방향 연결 불가능)
    - 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사 가능

목표
- 가장 높은 칸(들)에서 시작해 상하좌우 인접으로 이동하면서 항상 더 낮은 칸으로만 진행.
- 단, 경로 전체에서 단 1회에 한하여 어느 한 칸을 K 이하로 깎아 내려갈 수 있음.
- 가장 긴 경로 길이(방문 칸수)를 구함

전략
- 모든 최고 봉우리 좌표를 시작점으로 후보군 수집 --> 각 시작점에서 DFS(백트래킹)로 가능한 모든 단순 경로 탐색
- 이동은 두 가지 분기
    1. 그냥 하강 : next < current
    2. 한 번만 깎아서 하강 : not cut_used and next - K < current
    - 깍기 분기에서 그 칸을 딱 필요한 만큼만 current - 1로 임시 낮춘 뒤 재귀, 돌아오며 원복
"""
import sys
sys.stdin = open('sample_input.txt', 'r')

# 4방향
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def find_peaks(board, N):
    """보드에서 전역 최대값 좌표들을 (r, c) 형태로 모두 반환"""

    # 1) 전역 최대값(mx) 찾기
    mx = float('-inf')
    for r in range(N):
        for c in range(N):
            if board[r][c] > mx:
                mx = board[r][c]

    # 2) 최대값과 같은 칸들의 좌표를 수집
    peaks = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == mx:
                peaks.append((r, c))

    return peaks


def cut_length(N, K, board):
    peaks = find_peaks(board, N)
    visited = [[False]*N for _ in range(N)]
    best = 0

    def dfs(x, y, length, cut_used):
        nonlocal best
        best = max(best, length)

        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):  # 경계 먼저
                continue
            if visited[nx][ny]:
                continue

            # 1) 높은->낮은 정상 이동
            if board[nx][ny] < board[x][y]:
                visited[nx][ny] = True
                dfs(nx, ny, length + 1, cut_used)
                visited[nx][ny] = False

            # 2) 아직 안 깎았고, 깎으면 내려갈 수 있는 경우
            elif not cut_used and board[nx][ny] - K < board[x][y]:
                original = board[nx][ny]
                board[nx][ny] = board[x][y] - 1  # 꼭 필요한 만큼만 깎아 임시로 낮춤
                visited[nx][ny] = True
                dfs(nx, ny, length + 1, True)
                visited[nx][ny] = False
                board[nx][ny] = original        # 복구(백트래킹)

    for sr, sc in peaks:
        visited[sr][sc] = True
        dfs(sr, sc, 1, False)  # 시작 길이 1(자기 자신 포함)
        visited[sr][sc] = False

    return best


# ---- 메인 루프 ----
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = cut_length(N, K, board)
    print(f'#{tc} {ans}')
