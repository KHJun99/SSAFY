# [파이썬 S/W 문제해결 기본] 5일차 - 배열 최소 합
# SWEA 4881 배열 최소 합 - 백트래킹

import sys
sys.stdin = open('4881_input.txt')  # 로컬 테스트 시 사용


def dfs(row, cur_sum):
    global best

    # 가지치기: 현재 합이 이미 최적해 이상이면 더 진행할 필요 없음
    if cur_sum >= best:
        return

    # 모든 행에서 하나씩 선택 완료 -> 최솟값 갱신
    if row == N:
        best = cur_sum
        return

    # 현재 행에서 선택할 열을 탐색
    for c in range(N):
        if not used[c]:                 # 같은 열은 한 번만 사용
            used[c] = True
            dfs(row + 1, cur_sum + matrix[row][c])
            used[c] = False             # 백트래킹(되돌리기)


T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    used = [False] * N                  # 각 열 사용 여부
    best = float('inf')

    dfs(0, 0)
    print(f'#{tc} {best}')
