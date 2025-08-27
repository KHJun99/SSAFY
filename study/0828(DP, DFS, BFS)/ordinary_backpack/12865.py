# 백준_12865_평범한 배낭 (G5)
"""
- 문제 유형

전형적인 0/1 배낭 문제 (Knapsack Problem)

- 상황

물건의 개수: N
각 물건: 무게 W, 가치 V
배낭이 버틸 수 있는 최대 무게: K

- 목표

배낭에 담을 수 있는 물건들의 조합 중,
총 무게 ≤ K 를 만족하면서
총 가치의 합이 최대가 되는 값을 구하기.

- 핵심 조건

물건은 쪼갤 수 없음 (0/1 선택).
무게 한도를 넘으면 담을 수 없음.
"""

N, K = map(int, input().split())

thing = {}
for _ in range(N):
    W, V = map(int, input().split())
    thing[W] = V

max_val = float('-inf')

