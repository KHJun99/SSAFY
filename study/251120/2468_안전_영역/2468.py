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

# 비의 높이를 구하는 함수
def find_height():
    tmp_height = set()

    for r in range(N):
        for c in range(N):
            tmp_height.add(region[r][c])

    return list(tmp_height)


# 최대 안전 영역을 구하는 함수 (BFS)
def check_region(h_lst):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 최대 안전 영역 초기화
    max_safe_region = float('-inf')

    # 최대값을 구해야 하는 문제 -> 모든 높이 다 확인(브루트포스)
    for high in h_lst:
        visited = [[False] * N for _ in range(N)]
        queue = deque()
        ground = 0      # 영역의 개수를 세기 위한 변수 초기화

        # 물에 잠긴 위치 체크
        for r in range(N):
            for c in range(N):
                if region[r][c] <= high:
                    visited[r][c] = True

        # 물에 잠기지 않은 위치를 찾은 후 BFS 탐색
        for r in range(N):
            for c in range(N):
                if not visited[r][c]:
                    visited[r][c] = True
                    queue.append((r, c))

                    while queue:
                        cx, cy = queue.popleft()

                        for idx in range(4):
                            nx, ny = cx + dx[idx], cy + dy[idx]
                            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                                visited[nx][ny] = True
                                queue.append((nx, ny))

                    ground += 1

        # 최대 안전 영역 갱신
        if ground > max_safe_region:
            max_safe_region = ground

    return max_safe_region


N = int(input())
region = [list(map(int, input().split())) for _ in range(N)]

# 비가 안온 경우도 있기 때문에 0 추가
height = [0] + find_height()

result = check_region(height)

print(result)

