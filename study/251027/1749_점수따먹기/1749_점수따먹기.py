# 백준_1749_점수따먹기 (G4)
"""
## [문제 정리]
- 점수따먹기 게임
    - N * M 행렬을 그린다.
    - 각 칸에 -10,000 이상 10,000 이하의 정수를 하나씩 작성
    - 행렬의 부분행렬을 그려 그 안에 적힌 정수의 합을 구하는 게임

- 합이 최대가 되는 부분행렬을 구하는 프로그램을 작성하시오.
"""
N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

# 누적함을 저장할 배열 초기화
sum_arr = [[0] * (M + 1) for _ in range(N + 1)]

# 최대 누적값을 저장할 변수
max_value = float('-inf')
for r in range(1, N + 1):
    for c in range(1, M + 1):
        # 현재 칸까지의 합 = 위쪽 + 왼쪽 - 대각선(중복된 부분 제거) + 현재 값
        sum_arr[r][c] = sum_arr[r-1][c] + sum_arr[r][c-1] - sum_arr[r-1][c-1] + array[r-1][c-1]

        # 계산된 누적합 중 최댓값 갱신
        if max_value < sum_arr[r][c]:
            max_value = sum_arr[r][c]

print(max_value)
