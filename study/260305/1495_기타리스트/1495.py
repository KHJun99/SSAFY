# 백준_1495_기타리스트 (S1)
"""
## [문제 정리]

- 공연 시작 전에 볼륨을 바꿀 수 있는 리스트 생성
- V : 볼륨 리스트
    - V[i] : 곡을 연주하기 전에 바꿀 수 있는 볼륨
    - 항상 리스트에 적힌 차이로만 볼륨 변경 가능
    - 즉 현재 볼륨 P, i번째 곡을 연주하기 전
        - i 번째 곡은 P + V[i] or P - V[i]
        - but, 0보다 작은 값 or M 보다 큰 값으로는 변경 불가능

- 곡의 개수 N, 시작 볼륨 S, M이 주어졌을 때,
  마지막 곡을 연주할 수 있는 볼륨 중 최댓값을 구하시오.
  모든 곡은 리스트에 적힌 순서대로 연주
"""
N, S, M = map(int, input().split())

V = list(map(int, input().split()))

vol = [[0] * (M + 1) for _ in range(N + 1)]

vol[0][S] = 1

for i in range(N):
    for j in range(M + 1):
        if vol[i][j] == 1:
            min_vol = j - V[i]
            max_vol = j + V[i]

            if min_vol >= 0:
                vol[i + 1][min_vol] = 1

            if max_vol <= M:
                vol[i + 1][max_vol] = 1

result = -1

for i in range(M, -1, -1):
    if vol[N][i] == 1:
        result = i
        break

print(result)

