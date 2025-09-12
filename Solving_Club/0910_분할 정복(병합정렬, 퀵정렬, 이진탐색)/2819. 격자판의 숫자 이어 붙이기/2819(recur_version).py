# 격자판의 숫자 이어 붙이기 (D4)
"""
## [문제 요약]

- **격자판 크기**: 4×4 (총 16칸).
- **칸의 값**: 0 ~ 9 사이의 숫자.
- **이동 규칙**:
    1. 격자판의 아무 칸에서 시작.
    2. 동/서/남/북 방향으로 총 **6번 이동** → **7칸 방문**.
    3. 이동 경로의 칸에 적힌 숫자를 순서대로 이어 붙이면 **7자리 수**가 됨.
    4. 같은 칸을 여러 번 방문 가능.
    5. 시작 숫자가 0이어도 허용됨 (예: `0102001`).
    6. 격자판 밖으로는 이동 불가.

## [목표]

- 만들 수 있는 **서로 다른 7자리 수**들의 **개수**를 구하기.

## [접근 방법]

- 무조건 일곱 자리를 모두 붙여서 확인해야 한다.
    - 미리 계산 불가능한 문제
- 현재 좌표 기준 상하좌우 중 이동할 수 있는 곳으로 이동한다.
- 이때, 이동했던 경로들을 저장하면서 나아가야 한다.
    - DFS : 파라미터로 전달
    - BFS : 큐에 경로까지 함께 저장
"""
import sys
sys.stdin = open('sample_input.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# 1. 종료조건 : 숫자 7자리일 때 종료
# 2. 가지의 수 : 4개 (상하좌우)
def recur(y, x, number):
    if len(number) == 7:        # 7자리면 종료
        result.add(number)      # set 에 추가
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 밖이면 다음 방향 확인(continue)
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            continue

        # 다음 위치로 이동
        recur(ny, nx, number + matrix[ny][nx])


T = int(input())

for tc in range(1, T + 1):
    matrix = [input().split() for _ in range(4)]    # 숫자이지만 0이 처음에 들어 올 수 있으므로 문자로 받음
    result = set()

    # 7자리 만드는 코드
    # 4 * 4가 모두 출발점이 될 수 있다.
    for sy in range(4):
        for sx in range(4):
            recur(sy, sx, matrix[sy][sx])

    print(f'#{tc} {len(result)}')