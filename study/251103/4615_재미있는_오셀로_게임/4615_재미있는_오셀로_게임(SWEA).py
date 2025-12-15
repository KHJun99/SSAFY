# SWEA_4615_재미있는_오셀로_게임 (D3)
"""
## [문제 정리]
- 오셀로 게임
    - 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서
    - 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임
    - 보드는 4 x 4, 6 x 6, 8 x 8 크기를 사용
    - 게임 시작 시 보드 가운데 4칸에 W, B, B, W를 채우고 시작한다 (사각형 모양)
    - 플레이어는 빈 공간에 돌을 놓을 수 있다.
        - 단, 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 놓을 수 있다.
        - 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.
    - 만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.
    - 보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고
    - 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리한다.
"""
import sys
sys.stdin = open('sample_input(1).txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]

    # board 가운데 기본 돌
    mid = [(N // 2 - 1, N // 2 - 1), (N // 2 - 1, N // 2), (N // 2, N // 2 - 1), (N // 2, N // 2)]
    mid_val = ['W', 'B', 'B', 'W']
    for idx in range(4):
        nx, ny = mid[idx][0], mid[idx][1]
        board[nx][ny] = mid_val[idx]

    for _ in range(M):
        # doll = 1 : 흑돌, doll = 2 : 백돌
        c, r, doll = map(int, input().split())

    for row in board:
        print(row)