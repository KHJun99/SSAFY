# Stack 2 - 1 (후위표기, 백트래킹)
"""
조건
1. 오렌지와 블루는 서로 다른 복도에 있다.
2. 한 복도에는 1 이상 100 이하의 정수로 구분되는 100개의 버튼 존재
3. 버튼 K는 복도의 시작점에서 K미터 떨어져 있다.
4. 두 로봇은 버튼 1에서 시작
5. 매 1초마다, 로봇은 복도의 양 방향 중 하나로 1미터 걷거나, 자기 위치에 있는 버튼을 누르거나, 아무 것도 하지 않는다.
6. O, x : 오렌지가 해당 버튼 x를 눌러야 한다는 의미
7. B, x : 블루가 해당 버튼 x를 눌루야 한다는 의미
8. 순서대로 버튼을 눌러야 하기 때문에 동시에 누르지 못한다.

출력
- 테스트를 끝낼 수 있는 가장 빠른 시간
"""
# import sys
# sys.stdin = open('input.txt')
#
# T = int(input())
# for tc in range(1, T + 1):
#     button = list(map(str, input().split()))
#     N = button[0]
#     button.remove(N)
#
#     for idx in range(0, len(button), 2):
#     pass