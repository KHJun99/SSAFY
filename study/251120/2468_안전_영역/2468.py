# 백준_2468_안전_영역 (S1)
"""
## [문제 정리]
- 장마철에 내리는 비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정
- 물에 잠기는 지점을 회색으로 표시
- 물에 잠기지 않는 안전한 영역
    - 물에 잠기지 않은 지점들이 위, 아래, 오른쪽, 왼쪽으로 인접해 있다.
    - 그 크기가 최대인 영역
    - 꼭지점으로만 붙어 있는 두 지점은 인접하지 않는다고 취급
"""
from collections import deque


def find_height():
    tmp_height = set()

    for r in range(N):
        for c in range(N):
            tmp_height.add(region[r][c])

    return list(tmp_height)


def check_region():
    dx = [0, 1, 0, -1, -1, 1, 1, -1]
    dy = [1, 0, -1, 0, 1, 1, -1, -1]



N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]

height = find_height()

print(height)