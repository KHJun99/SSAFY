# SWEA_승자_예측하기 (D4)
"""
## [문제 정리]
- Alice 와 Bob이 게임을 하기로 했다.
- 게임 방법
    - 두 사람이 양의 정수 N을 정하고, 1로 초기화된 x를 가지고 있다.
    - Alice가 먼저 시작, 서로 번갈아 가면서 자신의 차례에 아래의 작업을 진행
        - x를 2x 또는 2x + 1로 대체
        - x가 N보다 커졌을 때 (초과) 그 작업을 한 사람이 패배
        - 예시 : N = 1일 때, Alice 는 2x, 2x+1 둘 중 어느것을 선택해도 1을 초과하기 떄문에 Bob 승리
        - N = 5일때, Alice가 2x+1을 선택하여 x = 3이 되면 Bob은 어떤 것을 선택해도 5 초과 -> Alice 승리

N이 주어질 때, 두 사람이 최선을 다해 게임을 한다면 누가 이기게 되는지 출력하는 프로그램 작성
"""
import sys
sys.stdin = open('sample_input.txt')

# 약 50퍼 gg
# def dfs(x, cnt):
#     if 2 * x > N:
#         return cnt - 1
#
#     win_A = (N // 2) + 1
#     win_B = (N // 2) - 1
#
#     a = 2 * x + 1
#     b = 2 * x
#
#     if a == win_A:
#         return dfs(a, cnt + 1)
#
#     elif b == win_B:
#         return dfs(b, cnt + 1)
#
#     else:
#         return dfs(b, cnt + 1)
#
# T = int(input())
#
# for tc in range(1, T + 1):
#     N = int(input())
#
#     result = dfs(1, 0)
#
#     if result % 2 == 0:
#         print(f'#{tc} Alice')
#     else:
#         print(f'#{tc} Bob')

