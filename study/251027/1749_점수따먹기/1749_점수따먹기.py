# 백준_1749_점수따먹기 (G4)
"""
## [문제 정리]
- 점수따먹기 게임
    - N * M 행렬을 그린다.
    - 각 칸에 -10,000 이상 10,000 이하의 정수를 하나씩 작성
    - 행렬의 부분행렬을 그려 그 안에 적힌 정수의 합을 구하는 게임

- 합이 최대가 되는 부분행렬을 구하는 프로그램을 작성하시오.
"""
# 누적합 사용, 틀림
# N, M = map(int, input().split())
#
# array = [list(map(int, input().split())) for _ in range(N)]
#
# # 누적함을 저장할 배열 초기화
# sum_arr = [[0] * (M + 1) for _ in range(N + 1)]
#
# # 최대 누적값을 저장할 변수
# max_value = float('-inf')
# for r in range(1, N + 1):
#     for c in range(1, M + 1):
#         # 현재 칸까지의 합 = 위쪽 + 왼쪽 - 대각선(중복된 부분 제거) + 현재 값
#         sum_arr[r][c] = sum_arr[r-1][c] + sum_arr[r][c-1] - sum_arr[r-1][c-1] + array[r-1][c-1]
#
#         # 계산된 누적합 중 최댓값 갱신
#         if max_value < sum_arr[r][c]:
#             max_value = sum_arr[r][c]
#
# print(max_value)


# 카데인 알고리즘 사용
def kadane_1d(arr):
    # 1차원 최대 연속 부분합 (모두 음수여도 동작)
    best = cur = arr[0]
    for i in range(1, len(arr)):
        x = arr[i]
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

NEG_INF = -10**18
ans = NEG_INF

# 행 압축 + 1D 카데인
for top in range(N):
    col_sum = [0] * M  # top이 바뀔 때마다 초기화
    for bottom in range(top, N):
        # top..bottom 사이 행들을 열별로 누적
        for c in range(M):
            col_sum[c] += A[bottom][c]
        # 누적된 열합 배열에서 최대 연속 부분합
        ans = max(ans, kadane_1d(col_sum))

print(ans)
