# SWEA_24396_공과_상자 (D3)
"""
## [문제 정리]
- B개의 검은 공, W개의 흰 공
- B개의 검은 상자, W개의 흰 상자
- 모든 공을 상자에 담아서, 모든 상자가 정확히 한 개의 공을 담고 있도록 하고자 한다.
- 모든 공을 강자에 넣으면, 아랭와 같이 각 상자마다 점수 계산
    - 검은 상자에 검은 공이 들어 있으면 X점
    - 흰 상자에 흰 공이 들어 있으면 Y점
    - 검은 상자에 흰 공 or 흰 상자에 검은 공이 있으면 Z점

-  모든 상자의 점수의 합이 최대화되도록 공을 넣었을 때
-  얻을 수 있는 최대 점수를 구하는 프로그램 작성
"""
import sys
sys.stdin = open('1_sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    B, W, X, Y, Z = map(int, input().split())

    cost1 = B * X + W * Y

    if B > W:
        cost2 = 2 * W * Z + (B - W) * X
    else:
        cost2 = 2 * B * Z + (W - B) * Y

    print(cost1) if cost1 >= cost2 else print(cost2)