# 정사각형 방 (D4)
"""
## [문제 요약]

- **격자 구조**: N×N 크기, 총 N²개의 방.
- **각 방의 값**: 1 이상 N² 이하의 정수, 모든 방의 값은 서로 다름.
- **이동 규칙**:
    1. 현재 방에서 상·하·좌·우로만 이동 가능.
    2. 이동하려는 방이 존재해야 함.
    3. 이동하려는 방의 숫자가 현재 방 숫자보다 정확히 **+1** 커야 이동 가능.

## [목표]

- 어떤 방에서 시작해야 가장 많은 방을 연속해서 이동할 수 있는지 찾기.
- 출력해야 하는 값:
    1. 시작 방의 숫자
    2. 이동할 수 있는 방의 **최대 개수**

## [접근 방법]

1. 모든 방에서 출발해 최대한 이동
    - 최악의 경우 사용 불가능
2. 배열을 만들어 표시
    - 1부터 $N^2$을 인덱스로 갖는 배열 A를 만든다.
    - 숫자 i의 인접에 1 큰 수가 있는 경우 A[i]에 1을 표시
    - 연속한 1의 개수가 최대인 경우를 찾는다.
"""
import sys
sys.stdin = open('input.txt', 'r')

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in  range(N)]
    visited = [0] * (N * N + 1)         # 1번 ~ N^2 번 방 번호

    # 현재 위치 숫자 기준 상하좌우를 확인
    # -> 1 큰게 있으면 visited 에 1이라고 체크
    for y in range(N):
        for x in range(N):
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                # 범위 밖 체크
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                if arr[ny][nx] == arr[y][x] + 1:
                    # 현재 숫자는 다음으로 이동 가능
                    visited[arr[y][x]] = 1
                    break # 다른 방향은 볼 필요 없다.

    # 연속된 1의 개수가 가장 긴 곳을 찾는다.
    max_cnt = 0     # 정답
    cnt = 0         # 하나하나 마다 몇 개가 연속되는지 확인하는 변수
    start = 0       # 숫자를 세기 시작한 위치
    for i in range(1, N * N + 1):
        if visited[i] == 1:
            cnt += 1
        else:       # 0을 만나면 계산
            if max_cnt < cnt:
                max_cnt = cnt       # 최대값 갱신
                start = i - cnt     # 시작점 찾기
            cnt = 0                 # 개수 초기화

    print(f'#{tc} {start} {max_cnt + 1}')